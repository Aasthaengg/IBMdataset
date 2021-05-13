N = int(input())
ans = 0
D = []

for i in range(N):
    d1, d2 = map(int, input().split())
    D.append([d1,d2])

for i in range(N-2):
    if D[i][0] == D[i][1]:
        if D[i+1][0] == D[i+1][1]:
            if D[i+2][0] == D[i+2][1]:
                ans = 1

if ans:
    print("Yes")
else:
    print("No")