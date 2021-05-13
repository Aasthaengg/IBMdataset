n, m = map(int, input().split())
num = [0] * n
sc = []
S = 0
C = 1
for i in range(m):
    s, c = map(int, input().split())
    # if num[s-1] != 0 and num[s-1] != c:
    #     print(-1)
    #     exit()
    # num[s-1] = c
    sc.append([s-1, c])

# if 1 < n and num[0] == 0:
#     print(-1)
#     exit()

for i in range(1000):
    ok = True
    string = str(i)
    if len(string) == n:
        for j in range(m):
            if string[sc[j][S]] != str(sc[j][C]):
                ok = False
                break
        if ok:
            print(i)
            exit()         
print(-1)