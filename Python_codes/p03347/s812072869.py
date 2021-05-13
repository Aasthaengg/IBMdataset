# 最初は0から始まる
# その次は、今の数+1以下である必要がある。
# 今の数+2以上が現れたらNG
# 通常は（0以外のときに）ans += 1
# 同じ数以下のとき、たとえば5 -> 3となっているときは、
# それまでに3を作れているはずなので、3を足す

N = int(input())
cur = 0
ans = 0
for i in range(N):
  a = int(input())
  if i == 0 and a != 0:
    print(-1)
    exit(0)
  elif a == 0:
    ans += 0
  elif a == cur + 1:
    ans += 1
  elif a <= cur:
    ans += a
  else:
    print(-1)
    exit(0)
  cur = a
print(ans)