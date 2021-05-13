import math
s = list(map(int, input().split()))
n=s[0]
k=s[1]-1
s = list(map(int, input().split()))
ind=s.index(1)
# print(ind,n-ind-1,math.ceil(ind/k),math.ceil((n-ind-1)/k))
print(math.ceil((n-1)/(k)))