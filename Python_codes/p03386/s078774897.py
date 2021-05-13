A, B, K = map(int, input().split())

if (B - A) // 2 < K:
    num_list = [i for i in range(A, B+1)]
    for i in num_list:
        print(i)
else:
    left = [i for i in range(A, A+K)]
    right = [i for i in range(B-K+1, B+1)]
    num_list = left + right
    for i in num_list:
        print(i)