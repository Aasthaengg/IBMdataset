H,W = map(int,input().split())
C = []
for _ in range(H):
    C.append(input())

ans = []
for c in C:
    for _ in range(2):
        ans.append(c)

for a in ans:
    print(a)