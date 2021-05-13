n = int(input())
ans = 0
for i in range(n):
    x,y = input().split()
    if y=="JPY": ans+=int(x)
    else: ans+=float(x)*380000
print(ans)