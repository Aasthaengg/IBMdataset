N = int(input())
T = [int(t) for t in input().split()]
A = [int(a) for a in input().split()]
mod = 7 + 10**9

TS, AS = [None for i in range(N)], [None for j in range(N)] #山の高さが一意に決まるならTrue
TS[0], AS[-1] = True, True
for i in range(1, N):
    if T[i] > T[i-1]: TS[i] = True
    else: TS[i] = False
    if A[N-1-i] > A[N-i]: AS[N-1-i] = True
    else: AS[N-1-i] = False

Ans = 1
for i in range(N): 
    if TS[i] and AS[i]:
        if T[i] != A[i]: 
            Ans = 0
            break
    elif TS[i]:
        if A[i] < T[i]:
            Ans = 0
            break
    elif AS[i]:
        if T[i] < A[i]:
            Ans = 0
            break
    else:
        Ans *= min(T[i], A[i])
        Ans %= mod

print(Ans)