# B - 1 21
a,b = map(int,input().split())
x = a*(10**len(str(b)))+b
ans = 'No'
for y in range(1000):
    if x==y*y:
        ans = 'Yes'
        break
print(ans)