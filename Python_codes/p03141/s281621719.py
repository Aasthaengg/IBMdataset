N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
ans = 0
S = []
for i in AB:
  ans -= i[1]
  S.append(i[0] + i[1])
S = sorted(S)[::-1]
for i in range(0,N,2):
  ans += S[i]
print(ans)