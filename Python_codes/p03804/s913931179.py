n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    a = list(input())
    A.append(a)
for i in range(m):
    b = list(input())
    B.append(b)

for i in range(n - m + 1):
    for j in range(n - m + 1):
        ok = True
        for h in range(m):
            if not ok:
                break
            for w in range(m):
                # print(A[i + h][j + w])
                if A[i + h][j + w] != B[h][w]:
                    ok = False
                    break
        if ok:
            print("Yes")
            exit()
print("No")