n=int(input())
V=list(map(int,input().split()))

V.sort()
avg=V[0]
for i in range(n):
  avg = (avg +V[i]) /2
  
print(avg)