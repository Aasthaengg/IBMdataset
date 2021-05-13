N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

p = 0
for i in range(N)[::-1]:
  a,b = AB[i]
  a += p
  p += 0 if a % b == 0 else b - a % b
  
print(p)
