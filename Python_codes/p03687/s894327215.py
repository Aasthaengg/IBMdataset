s = input()
N = len(s)

a = ord('a')

check = [[False for j in range(26)] for i in range(N)]

for i in range(N):
    check[i][ord(s[i])-a] = True

for j in range(26):
    same = True
    for i in range(N):
        if not check[i][j]:
            same = False
    if same:
        print(0)
        exit()

ans = 1
while True:
    for i in range(N-ans):
        for j in range(26):
            if check[i][j] or check[i+1][j]:
                check[i][j] = True
    for j in range(26):
        same = True
        for i in range(N-ans):
            if not check[i][j]:
                same = False
        if same:
            print(ans)
            exit()
    ans += 1

