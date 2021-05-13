from bisect import bisect_right,bisect_left
n=int(input())
A=sorted(list(map(int,input().split())))
B=list(map(int,input().split()))
C=sorted(list(map(int,input().split())))

ans=0
for b in B:
    a_index=bisect_left(A,b)
    c_index=bisect_right(C,b)
    ans +=a_index*(n-c_index)

print(ans)