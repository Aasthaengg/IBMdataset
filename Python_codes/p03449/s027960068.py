import sys
input = sys.stdin.readline

N =int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

sumA1 = A1[0]
sumA2 = sum(A2)
total = sumA1 + sumA2
ans = total
for i in range(1,N):
    sumA1 += A1[i]
    sumA2 -= A2[i-1]
    total = sumA1+sumA2
    ans = max(ans,total)
print(ans)
    
