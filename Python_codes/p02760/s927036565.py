a, b, c = [],[],[]
ans = "No"
num = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
for _ in range(3):
    n = list(map(int,input().split()))
    for i in range(3):
        a.append(n[i])
        
n = int(input())
for j in range(n):
    b.append(int(input()))
    
for k in range(9):
    for l in b:
        if a[k] == l:
            c.append(int(k))

for m in range(8):
    q = 0
    for p in range(3):
        if num[m][p] in c:
            q += 1
    if q == 3:
        ans = "Yes"
print(ans)