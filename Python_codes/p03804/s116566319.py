n, m = map(int, input().split())
N = []
M = []
for i in range(n):
    N.append(input())
for i in range(m):
    M.append(input())

for i in range(n-m+1):
    if not M[0] in N[i]:
        continue
    else:
        pos = N[i].index(M[0])
        flag = True
        for j in range(m):
            if M[j] != N[i+j][pos:pos+m]:
                flag = False
                break
        if flag:
            print("Yes")
            exit()
print("No")