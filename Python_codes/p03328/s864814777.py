a,b = map(int,input().split())
div = b-a
ans = 0
for i in range(1,1000):
    if div==i:
        break
    ans += i
print(ans-a)