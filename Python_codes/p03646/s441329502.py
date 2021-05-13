K=int(input())
n=50
t=K//50
r=K%50
a=49+t
s=[a]*n
for i in range(r):
    for j in range(n):
        if j==n-i-1:
            s[j]+=n
        else:
            s[j]-=1
print(n)
print(*s)
