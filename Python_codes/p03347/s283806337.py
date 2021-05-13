N = int(input())
A = [int(input()) for _ in range(N)]

def main(N, A):
    if A[0] != 0: return -1
    if any([A[i+1] - A[i] > 1 for i in range(N-1)]): return -1
    A.reverse()
    ans = 0
    before = -1
    for a in A:
        if a+1 != before:
            ans += a
        before = a
    return ans

print(main(N, A))
