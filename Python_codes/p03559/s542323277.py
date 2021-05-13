import bisect
N=int(input())
A=sorted(list(map(int, input().split())))
B=sorted(list(map(int, input().split())))
C=sorted(list(map(int, input().split())))
#真ん中を固定
ans=0
for i in range(N):
    b=B[i]
    ab=bisect.bisect_left(A,b)
    bc=N-bisect.bisect_right(C,b)
    ans+=ab*bc
print(ans)