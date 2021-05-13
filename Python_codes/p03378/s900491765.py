n, m, x = map(int, input().split())
a = list(map(int, input().split()))
pr = 0 ; pl = 0
for i in range(x,n+1) :
    if i in a :
        pr += 1
for j in range(x,-1,-1) :
    if j in a :
        pl += 1
mn = min(pr, pl)
print(mn)
