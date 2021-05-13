from bisect import bisect_left,bisect_right
n=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
C=sorted(list(map(int,input().split())))

ans=0
for i in B:
    ans +=bisect_left(A,i)*(n-bisect_right(C,i))
print(ans)