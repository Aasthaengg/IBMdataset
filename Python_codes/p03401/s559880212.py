N = int(input())
A = list(map(int, input().split()))
ans = abs(A[0])
ans += sum([abs(A[i]-A[i-1]) for i in range(1, N)])
ans += abs(A[-1])

for i in range(N):
    if i == 0:
        if (0 <= A[i] <= A[i+1]) or (A[i+1] <= A[i] <= 0):
            tmp = ans 
        else:
            tmp = ans - abs(A[0]) - abs(A[0]-A[1]) + abs(A[1])
        print(tmp)
    elif i == N-1:
        if (0 <= A[i] <= A[i-1]) or (A[i-1] <= A[i] <= 0):
            tmp = ans
        else:
            tmp = ans - abs(A[i]-A[i-1]) - abs(A[i]) + abs(A[i-1])
        print(tmp)
    else:
        if (A[i-1] <= A[i] <= A[i+1]) or (A[i-1] >= A[i] >= A[i+1]):
            print(ans)
        else:
            tmp = ans - abs(A[i]-A[i-1]) - abs(A[i]-A[i+1]) + abs(A[i+1]-A[i-1])
            print(tmp)