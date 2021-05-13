from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.sort()

# A[cut-1] < 0 and A[cut] >= 0
cut = 0
while cut < N and A[cut] < 0:
    cut += 1

if cut == 0:
    M = sum(A[1:]) - A[0]
    print(M)
    pair = [A[0], A[N-1]]
    for i in range(N-2):
        print(' '.join(map(str, pair)))
        pair = [pair[0] - pair[1], A[N-i-2]]
    pair.reverse()
    print(' '.join(map(str, pair)))

elif cut == N:
    M = A[-1] - sum(A[:N-1])
    print(M)
    pair = [A[N-1], A[0]]
    for i in range(N-2):
        print(' '.join(map(str, pair)))
        pair = [pair[0] - pair[1], A[i+1]]
    print(' '.join(map(str, pair)))

else:
    M = sum(A[cut:]) - sum(A[:cut])
    print(M)

    B = deque(A[cut:]) # Aの正の部分
    C = deque(A[:cut]) # Aの負の部分

    while len(B) != 1:
        pair = [C[-1], B[-1]]
        print(' '.join(map(str, pair)))
        b = B.pop()
        C[-1] = C[-1] - b
    
    b = B.pop()

    while len(C) != 0:
        pair = [b, C[0]]
        print(' '.join(map(str, pair)))
        c = C.popleft()
        b = b - c