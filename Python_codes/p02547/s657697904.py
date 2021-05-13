N = int(input())
a = 0
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1==D2:
        a += 1
    else:
        a = 0
    if a == 3:
        print("")
        print("Yes")
        break
    if i == N-1 and a != 3:
        print("No")