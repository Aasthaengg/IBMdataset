N,K = list(map(int, input().split()))
S = input()
# 0の塊をK回返して、1の連結をつくる
# K = 2 のとき
# ... 0:3,1:3,0:2,1:2,0:3,1:4,0:2,... のとき
# 1:2の両端をを返す→1始まりの5個の部分和
# 1の塊をK-1回返して、0の連結をつくり、最後にひっくり返す（端の1ともくっつく…）
# K = 2 のとき
# ... 0:3,1:3,0:2,1:2,0:3,1:4,0:2,... のとき
# 1:2を裏返す、0:2-1:2-0:3を返す　→　あれ一緒…？


# 0が端のときだけ気を付ければよさそう…
# 0が端にあったらひっくり返したA作って、Kを減らしておなじことやりゃよいのか？
# あとKが極端に小さいか、Arrayの数（0/1のパターン数より大きいとき）の考慮
# あとlen(A) = 1

# sequence数を格納するArrayを作る
A = []
pre = S[0]
cnt = 1
for i in range(1,N):
  now = S[i]
  if pre == now:
    cnt += 1
  else:
    A.append(cnt)
    cnt = 1
  pre = now
A.append(cnt)

#print(A)

if len(A) == 1:
  print(sum(A))
  exit(0)

# 貪欲でとってから前2個足して後ろ引く、見たいにやればO(N)でいけるはず…
# 部分和でも仕留められそうではあるけど…
def solve(Ar,Kr):
  l,r = 0, 2*Kr+1
  if len(Ar) < 2*Kr+1:
    #全部でよい
    return sum(Ar)
  wk = sum(Ar[l:r])
  ans = wk
  while r < len(Ar):
    wk = wk - Ar[l] - Ar[l+1] + Ar[r] + (Ar[r+1] if r+1 < len(Ar) else 0)
    ans = max(ans, wk)
    #print(wk,l,r,Ar[l],Ar[r])
    l,r = l+2, r+2
  return ans

if S[0] == '1':
  print(solve(A,K))
else:
  B = A[1:]
  B[0] += A[0] # 1始まりに無理やりする
  print(max(solve(A[1:],K), solve(B,K-1)))