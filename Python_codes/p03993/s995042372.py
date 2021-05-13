n = int(input())
a_l = list(map(int, input().split()))

ans = 0
for i,j in enumerate(a_l):
    if i+1 == a_l[j-1]:
        ans+= 1
print(int(ans/2))