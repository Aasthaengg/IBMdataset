n,k = map(int,input().split())
A = list(map(int,input().split()))
bi = ''
cur = 1
while cur <= k:
    t = k&cur
    if t != 0:
        bi = '1'+bi
    else:
        bi = '0'+bi
    cur *= 2
bit = [0]*len(bi)
for i in range(n):
    u = A[i]
    cur = 1
    s = ''
    times = 0
    for j in range(40):
        z = u&cur
        if z != 0:
            if times < len(bi):
                bit[len(bi)-times-1] += 1
        cur *= 2
        times += 1
ans = ''
flag = False #kを下回っているかどうか
l = len(A)
if l%2 != 0:
    for i in range(len(bi)):
        if l//2 < bit[i]:
            if flag:
                ans = ans+'0'
            else:
                if bi[i] == '1':
                    flag = True
                    ans = ans+'0'
                else:
                    ans = ans+'0'
        else:
            if flag:
                ans = ans+'1'
            else:
                if bi[i] == '1':
                    ans = ans+'1'
                else:
                    ans = ans+'0'
else:
    for i in range(len(bi)):
        if l//2 <= bit[i]:
            if flag:
                ans = ans+'0'
            else:
                if bi[i] == '1':
                    flag = True
                    ans = ans+'0'
                else:
                    ans = ans+'0'
        else:
            if flag:
                ans = ans+'1'
            else:
                if bi[i] == '1':
                    ans = ans+'1'
                else:
                    ans = ans+'0'
alt = 0
cur = 1
for i in range(len(ans)):
    if ans[len(ans)-i-1] == '1':
        alt += cur
    cur *= 2
S = 0
for i in range(n):
    S += A[i]^alt
print(S)
