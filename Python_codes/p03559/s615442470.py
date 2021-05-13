import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()
ans = 0
#順序維持のbisect (二分探索を利用したライブラリ）
for i in range(N):
    count_a = bisect.bisect_left(A,B[i])
    count_c = N -bisect.bisect_right(C,B[i])
    ans += count_a*count_c
print(ans)