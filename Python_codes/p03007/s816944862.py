N = int(input())
A = [int(s) for s in input().split(' ')]
A.sort()
print(A[N - 1] + sum([abs(a) for a in A[1:N - 1]]) - A[0])
answer = ''
for i in range(1, len(A) - 1):
    if(A[i] > 0):
        answer += "{} {}\n".format(A[0], A[i])
        A[0] -= A[i]
    else:
        answer += "{} {}\n".format(A[N - 1], A[i])
        A[N - 1] -= A[i]
answer += "{} {}\n".format(A[N - 1], A[0])
print(answer)