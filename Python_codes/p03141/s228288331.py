n = int(input())

dish = []
ans = 0
for i in range(n):
    a, b = map(int,input().split())
    ans -= b
    dish.append(a+b)
dish.sort(reverse=True)    

for i in range(n):
    if not i%2:
        ans += dish[i]
        
print(ans)