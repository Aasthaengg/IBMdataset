N = int(input())
S = input()
T = input()
C = 10**9+7

flag = [False]*N
if S[0] == T[0]:
    ct = 3
    flag[0] = True
    i = 1
else:
    ct = 6
    i = 2
while i < N:
    if S[i] == T[i]:
        flag[i] = True
        if flag[i-1]:
            ct *= 2
        i += 1
    else:
        if flag[i-1]:
            ct *= 2
        else:
            ct *= 3
        i += 2
    ct = ct % C
    # print(i,ct)
print(ct)
