n=input()
A=list(map(int,input().split()))
o=sum(a%2 for a in A)
print("NO" if o%2 else "YES")