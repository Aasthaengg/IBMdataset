def ch(x):
    return ord(x)-ord("a")
def dch(x):
    return chr(x+ord("a"))

S = input().rstrip()
T = input().rstrip()

s0 = S[0]
cnt = 1
A1 = []
P = [-1]*26
k=0
for s in S[1:]:
    if s==s0:
        cnt += 1
    else:
        if P[ch(s0)] == -1:
            P[ch(s0)] = k
            k += 1
            A1.append((P[ch(s0)], cnt))
        else:
            A1.append((P[ch(s0)], cnt))
        cnt = 1
    s0 = s
if cnt == 1:
    if P[ch(s0)] == -1:
        P[ch(s0)] = k
        k += 1
        A1.append((P[ch(s0)], cnt))
    else:
        A1.append((P[ch(s0)], cnt))

t0 = T[0]
cnt = 1
B1 = []
P = [-1]*26
k=0
for t in T[1:]:
    if t==t0:
        cnt += 1
    else:
        if P[ch(t0)] == -1:
            P[ch(t0)] = k
            k += 1
            B1.append((P[ch(t0)], cnt))
        else:
            B1.append((P[ch(t0)], cnt))
        cnt = 1
    t0 = t
if cnt == 1:
    if P[ch(t0)] == -1:
        P[ch(t0)] = k
        k += 1
        B1.append((P[ch(t0)], cnt))
    else:
        B1.append((P[ch(t0)], cnt))

if A1==B1:
    print("Yes")
else:
    print("No")


