def c_marks():
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    ans = ['Yes' if A[i + K] > A[i] else 'No' for i in range(N - K)]
    return '\n'.join(ans)

print(c_marks())