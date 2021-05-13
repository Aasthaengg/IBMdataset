N = int(input())
AB = []
ans = 0
for _ in range(N):
  a,b = map(int,input().split())
  AB.append(a+b)
  ans -= b
AB.sort(reverse=True)

print(ans+sum(AB[::2]))