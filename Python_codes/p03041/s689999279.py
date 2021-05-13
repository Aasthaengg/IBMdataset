n,k=map(int,input().split())
s=list(str(input()))

s[k-1]=chr(ord(s[k-1])+32)
ans=("").join(s)
print(ans)