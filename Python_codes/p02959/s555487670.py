n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split())) + [0]

bonus = 0
x = 0
for i in range(n+1):
    enemy = max(0, a[i] - bonus) 
    tmp = enemy - b[i]
    if tmp <= 0:
        x += a[i]
        bonus = -tmp
    else:
        x += (b[i] + bonus)
        bonus = 0

print(x)