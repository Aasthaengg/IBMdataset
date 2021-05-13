n = int(input())
h = [int(xi) for xi in input().split()]

stock = 0
ans = "Yes"

for xi in range(n-1):
    stock += h[xi+1]-h[xi]
    if stock<0:
        ans = "No"
        break
    if stock>1: stock=1

print(ans)
