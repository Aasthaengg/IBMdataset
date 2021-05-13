s=input().split()
n=int(s[0])
k=int(s[1])
if k ==1:
    print(0)
else:
    mx=n-k+1
    mn=1
    print(mx-mn)
