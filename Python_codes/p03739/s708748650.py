n = int(input())
a = list(map(int, input().split()))

S = 0
C = 0
S = a[0]
if S > 0:
    pm = 1
elif S < 0:
    pm = 0
else:
    S += 1
    C += 1
    pm = 1
for i in range(1, n):
    S += a[i]
    if pm == 1 and S >= 0:
        C += S + 1
        S -= S + 1
    elif pm == 0 and S <= 0:
        C += -S + 1
        S += -S + 1
    pm = 1 - pm 

T = 0
D = 0
T = a[0]
if T > 0:
    D += T + 1
    T -= T + 1
    pm = 0
elif T < 0:
    D += -T + 1
    T += -T + 1
    pm = 1
else:
    T -= 1
    D += 1
    pm = 0
for i in range(1, n):
    T += a[i]
    if pm == 1 and T >= 0:
        D += T + 1
        T -= T + 1
    elif pm == 0 and T <= 0:
        D += -T + 1
        T += -T + 1
    pm = 1 - pm

print(min(C, D))