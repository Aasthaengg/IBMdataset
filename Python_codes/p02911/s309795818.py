def resolve():
    N, K, Q = list(map(int, input().split()))
    A = [int(input()) for _ in range(Q)]
    points = [0 for _ in range(N)]
    for a in A:
        points[a-1] += 1
    for p in points:
        print("Yes" if Q-K<p else "No")


    
if '__main__' == __name__:
    resolve()