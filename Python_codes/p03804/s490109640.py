a, b = map(int,input().split())
A = [input() for _ in range(a)]
B = [input() for _ in range(b)]
ans = "No"
for i in range(a-b+1):
    for j in range(a-b+1):
        cnt = 0
        if A[i][j] == B[0][0]:
            for k in range(b):
                for l in range(b):
                    if A[i+k][j+l] == B[k][l]:
                        cnt += 1
                    if cnt == b**2:
                        ans = "Yes"

print(ans)