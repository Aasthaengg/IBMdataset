import bisect
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
count = 0
for j in range(N):
    c = N-bisect.bisect_right(C,B[j])
    b = bisect.bisect_right(A,B[j]-1)
    count += b*c
print(count)