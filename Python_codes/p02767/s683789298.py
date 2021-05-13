n = int(input())
x =  list(map(int,input().split()))

x.sort()

ans = 1000000000

for i in range(101):
    hp = 0
    for j in x:
        hp += (j-i)**2
    ans = min(ans,hp)
print(ans)