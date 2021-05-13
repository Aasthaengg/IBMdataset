n=int(input())
a=list(map(int,input().split()))
even=len([i for i in a if i%2==0])
All = pow(3,n)
#すべてoddをひく
t = pow(2,even)
print(All-t)