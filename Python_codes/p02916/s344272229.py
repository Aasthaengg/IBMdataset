n=int(input())
a=[int(_) for _ in input().split()]
b=[int(_) for _ in input().split()]
c=[int(_) for _ in input().split()]
r=0
for i in range(1,len(a)):
    if a[i]-a[i-1] == 1:
        r+=c[a[i-1]-1]
print(sum(b)+r)