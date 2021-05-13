N = int(input())
A = list(map(int,input().split()))
number = [0 for _ in range(N)]

for i, a in enumerate(A):
  number[a-1] += i+1
  
print(*number)