n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [a-b for a,b in zip(A,B)]
A.sort()
if sum(A)<0:
    print(-1)
else:
    cnt = sum([a<0 for a in A])
    max_i = -1
    for i in range(n):
        while A[i]<0:
            if A[max_i] > abs(A[i]):
                A[max_i] += A[i]
                A[i] = 0
            else:
                A[i] += A[max_i]
                A[max_i] = 0
                max_i -= 1
    print(cnt-max_i if cnt!=0 else 0)