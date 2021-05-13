N = input()
T = map(int,raw_input().split(" "))
A = map(int,raw_input().split(" "))




note = [1 for i in range(N)]
fx = [0 for i in range(N)]

def solve():
    global note
    if T[-1] != A[0]:
        return 0
    
    prev = 0
    for i in range(N):
        if prev > T[i]:
            return 0
        elif prev == T[i]:
            note[i] = prev
        else:
            note[i] = 1
            prev = T[i]
            fx[i] = T[i]
    prev = 0
    for i in range(N-1,-1,-1):
        if prev > A[i]:
            return 0
        elif prev == A[i]:
            if not fx[i]:
                note[i] = min(note[i],prev)
            else:
                if fx[i] > A[i]:
                    return 0

        else:
            if fx[i] and fx[i] != A[i]:
                return 0
            note[i] = 1
            prev = A[i]

    ans = 1
    for i in range(N):
        if not fx[i]:
            ans = (ans * note[i])%(10**9+7)
    return ans



    





print solve()
