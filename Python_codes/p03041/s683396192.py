n,k=[int(s) for s in input().split()]
s=input()
# s[k-1]=s[k-1].lower()
print(s[:k-1]+s[k-1].lower()+s[k:])