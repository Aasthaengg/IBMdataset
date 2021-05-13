import sys

n = int(input())

a = []

for _ in range(n):
    A = list(map(int, input().split( )))
    a.append(A)

b = [[a[i][j] for j in range(n)] for i in range(n)]

#三角不等式(等号可)を満たしてなかったら無理
#満たしてた場合、どの迂回路とも真の不等号ならば保持

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] + a[k][j] < a[i][j]:
                print(-1)
                sys.exit()
            if i!=k and j!=k and a[i][k] + a[k][j] == a[i][j]:

                b[i][j] = 0
ans = 0
for i in range(n):
    ans += sum(b[i])

print(ans//2)


