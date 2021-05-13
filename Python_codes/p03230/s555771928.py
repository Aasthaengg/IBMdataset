N = int(input())
hoge = 0
M = 1
while True:
    hoge += M
    if hoge == N:
        print("Yes")
        break
    if hoge > N:
        print("No")
        exit()
    M += 1
print(M+1)

ans = []
hoge = 1
for i in range(M):
    ans.append([])
    for j in range(i+1):
        ans[-1].append(hoge)
        hoge += 1
for i in range(M):
    print(M,end = " ")
    for j in range(i+1):
        print(ans[i][j],end = " ")
    for j in range(i+1,M):
        print(ans[j][i],end=" ")
    print()
print(M,end=" ")
for i in range(M):
    print(ans[i][i],end=" ")
print()