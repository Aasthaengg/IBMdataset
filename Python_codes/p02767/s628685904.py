n = int(input())
x = list(map(int,input().split()))
HP = 10**6
for i in range(1,101):
    hp = 0
    for j in range(n):
        hp += (i - x[j])**2
    HP = min(HP,hp)
print(HP)