N = int(input())
A = list(map(int,input().split()))

A2 = [0]*N

i =1
for a in A:
  A2[a-1] = i
  i+=1

print(*A2)