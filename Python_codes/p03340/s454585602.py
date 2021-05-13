n = int(input())
A = list(map(int, input().split()))

ans = 0
t = 0
S = [0]*30

def func(cur, S):
    cur_bi = list(format(cur, 'b'))
    cur_bi = list(reversed(cur_bi))
    flag = True
    for i in range(len(cur_bi)):
        if cur_bi[i] == '1' and S[i] == 1:
            flag = False
            break
    return flag

for s in range(n):
    while t < n and func(A[t], S):
        cur = A[t]
        cur_bi = list(format(cur, 'b'))
        cur_bi = list(reversed(cur_bi))
        for i in range(len(cur_bi)):
            if cur_bi[i] == '1':
                S[i] = 1
        t += 1
    ans += t-s
    if s == t:
        t += 1
    else:
        cur = A[s]
        cur_bi = list(format(cur, 'b'))
        cur_bi = list(reversed(cur_bi))
        for i in range(len(cur_bi)):
            if cur_bi[i] == '1':
                S[i] = 0

print(ans)