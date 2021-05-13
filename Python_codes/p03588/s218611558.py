N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
AB = sorted(AB)
#print(AB)
ans = N + AB[-1][1]
for i in range(N):
  if i == 0:
    ans += AB[0][0] - 1
  else:
    ans += min(abs(AB[i][0]-AB[i-1][0])-1,abs(AB[i][1]-AB[i-1][1])-1)
print(ans)