n,k=map(int,input().split())
k-=1
s=input()
print(s[:k]+s[k].lower()+s[k+1:])
