S = input()

N = len(S)
tcnt =[0] * 128
for c in S:
    tcnt[ord(c)] += 1 if c != 'x' else 0
odd = 0
for i in range(128):
    if tcnt[i] % 2 == 1:
        if odd != 0:
            print(-1)
            exit()
        else:
            odd = i

cl = -1
cr = -1
cnt = [0] * 128
for i in range(N):
    cnt[ord(S[i])] += 1 if S[i] != 'x' else 0
    if cnt[ord(S[i])] > (tcnt[ord(S[i])] + 1) // 2:
        cr = i
        break
    elif S[i] != 'x':
        cl = i
if cl == -1:
    print(0)
    exit()

if odd != 0:
    cr = cl

ans = 0
while cl >= 0 and cr < N:
    l = cl - 1
    while l >= 0 and S[l] == 'x':
        l -= 1
    lx = cl - l - 1
    r = cr + 1
    while r < N and S[r] == 'x':
        r += 1
    rx = r - cr - 1
    ans += abs(lx - rx)

    a = ord(S[l]) if l >= 0 else 0
    b = ord(S[r]) if r < N else 0
    if a != b:
        print(-1)
        exit()
    else:
        cl = l
        cr = r

print(ans)