import bisect
N = int(input())
if len(str(N)) == 1:
    print(N)
    exit()
L = len(list(str(N)))-1
A = [10**(L)*i+10**(L)-1 for i in range(10)]  
n = bisect.bisect_left(A,N)-1
if N in A:
    n += 1
ans = [int(list(str(A[n]))[i]) for i in range(len(list(str(A[n]))))]
print(sum(ans))
