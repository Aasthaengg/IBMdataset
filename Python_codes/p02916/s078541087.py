N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
memo = -100
for i in range(N):
  dish = A[i]
  base = B[dish - 1]
  ans += base
  if dish - memo == 1:
    ans += C[dish - 2]
  memo = dish
  
    
print(ans)