N, A, B = map(int, input().split())

if abs(A-B) % 2 == 0:
    print(abs(A-B)//2)
else:
    M = max(A, B)
    m = min(A, B)
    print(min(N-m, M-1, (N-M+1)+(M-m)//2, m+(M-m)//2))