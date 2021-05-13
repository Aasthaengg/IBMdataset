a,b = map(int,input().split())
ans = 0

for i in range(1,1001):
    if i*8//100  == a and i//10 == b:
        ans = i
        break
else:
    ans = -1

print(ans)