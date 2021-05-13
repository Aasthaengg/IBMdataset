A,B = map(int, input().split())

h = 100
w = 100
ans = [["#"]*w for _ in range(h)]
for i in range(h):
    for j in range(w//2):
        ans[i][j] = "."
    
L = [0, 0]
for i in range(B-1):
    r = L[0]
    c = L[1]
    ans[r][c] = "#"
    L[1] += 2
    if L[1] >= 50:
        L[0] += 2
        L[1] = 0
    
L = [0, 99]
for i in range(A-1):
    r = L[0]
    c = L[1]
    ans[r][c] = "."
    L[1] -= 2
    if L[1] <= 50:
        L[0] += 2
        L[1] = 99
    
print(h, w)
for i in range(h):
    print("".join(ans[i]))