n = int(input())

A =[int(x) for x in input().split()]
B =[int(x) for x in input().split()]
C =[int(x) for x in input().split()]

ans = 0
ans = sum(B)

for i in range(n-1):
    
    if((A[i]+1)==A[i+1]):
        ans += C[A[i]-1]
print(ans)