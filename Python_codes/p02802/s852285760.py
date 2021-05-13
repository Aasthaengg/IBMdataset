N, M = map(int,input().split())
AC_list = [0 for _ in range(N)]
WA_list = [0 for _ in range(N)]


for i in range(M):
    # print(AC_list)
    # print(WA_list)
    p, S = map(str,input().split())
    p = int(p)-1
    if S == "AC" and AC_list[p] == 0:
        AC_list[p] = 1
    elif S == "WA" and AC_list[p] == 0:
        WA_list[p] +=1
    else:
        continue

for i in range(N):
    if AC_list[i] == 0:
        WA_list[i] = 0

print("{} {}".format(sum(AC_list), sum(WA_list)))