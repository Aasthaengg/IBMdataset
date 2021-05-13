# N = int(input())
N, A, B = [int(_) for _ in input().split()]
if (B - A) % 2 == 0:
    print((B-A) // 2)
else:
    print(min(N - B + 1 + (N - (A + N-B+1)) // 2, A + (B - A - 1)//2))
