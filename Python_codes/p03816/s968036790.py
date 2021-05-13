from collections import Counter
input()
A=list(map(int,input().split()))
c=Counter(A)
lenc=len(c)
print(lenc-1 if lenc&1==0 else lenc)
