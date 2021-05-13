n = int(input())
A = [0] + list(map(int, input().split())) + [0]
work = [0 for i in range(n)]
count = 0
for i in range(1, n+1):
    if (A[i]-A[i-1])*(A[i+1]-A[i]) < 0:
        work[i-1] = min(abs(A[i+1] - A[i])*2, abs(A[i] - A[i-1])*2)
    count += abs(A[i]-A[i-1])
count += abs(A[n]-0)
for el in work:
    print(count-el)