n, m = map(int, input().split())

l = list()
la = [0] * (n+1)
ln = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        la[b] = 1
    elif b == 1:
        la[a] = 1
    if a == n:
        ln[b] = 1
    elif b == n:
        ln[a] = 1

for i in range(n+1):
    if la[i]*ln[i] == 1:
        print("POSSIBLE") 
        exit()

print("IMPOSSIBLE")