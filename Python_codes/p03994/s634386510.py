S=input()
K=int(input())
c2i=lambda c: ord(c)-ord("a")
i2c=lambda i: chr(i+ord("a"))
A=list(map(c2i, S))
for i in range(len(A)):
    if A[i] and 26-A[i]<=K:
        K-=26-A[i]
        A[i]=0
A[-1]+=K
A[-1]%=26
print("".join(map(i2c,A)))