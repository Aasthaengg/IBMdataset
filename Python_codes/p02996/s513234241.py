N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
A.sort(key = lambda x: x[1])
su = 0
for i in A:
    su += i[0]
    if su > i[1]:
        print("No")
        exit()
print("Yes")