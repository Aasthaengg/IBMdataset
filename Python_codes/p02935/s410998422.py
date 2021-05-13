n=int(input())
v=[int(x) for x in input().split()]

v.sort()

ans=(v[0]+v[1])/2

for i in range(2,n):
    ans=(ans+v[i])/2
print(ans)