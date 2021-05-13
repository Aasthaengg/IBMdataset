n = int(input())
A = list(map(int, input().split()))
r = 0
for i in range(n):
    if A[i]%2==0:
        r+=1
print(3**n-2**r)