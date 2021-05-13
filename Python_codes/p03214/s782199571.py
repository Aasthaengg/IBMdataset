n=int(input())
a = list(map(int,input().split()))	
h=sum(a)/n
value=sum(a)
index=0
for i in range(n):
    if value > abs(a[i] - h):
        value = abs(a[i] - h)
        index = i
print(index)

