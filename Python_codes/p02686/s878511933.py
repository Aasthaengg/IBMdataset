N = int(input())
S = [input() for _ in [0]*N]

A = [(0,0)]*N
B = [(0,0)]*N
for i,T in enumerate(S):
    m = 0
    M = 0
    tot = len(T) - T.count(")")*2
    if tot>=0:
        tot = 0
        for t in T:
            if t==")":
                tot -= 1
                m = min(m,tot)
            else:
                tot += 1
        A[i] = (m,tot)
    else:
        tot = 0
        for t in T[::-1]:
            if t==")":
                tot += 1
            else:
                tot -= 1
                m = min(m,tot)
        B[i] = (m,tot)

A.sort(reverse=True)
B.sort(reverse=True)

totA = 0
ans = True
for m,t in A:
    if totA + m < 0:
        ans = False
        break
    totA += t
totB = 0
if ans:
    for m,t in B:
        if totB + m < 0:
            ans = False
            break
        totB += t
    if totA != totB:
        ans = False

if ans:
    print("Yes")
else:
    print("No")