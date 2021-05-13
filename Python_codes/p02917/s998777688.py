import copy
n = int(input())
b = list(map(int,input().split()))
a = copy.copy(b)
a.insert(0,b[0])
for i in range(n-2):
    a[i+1]=min(b[i],b[i+1])
#print(b)
print(sum(a))