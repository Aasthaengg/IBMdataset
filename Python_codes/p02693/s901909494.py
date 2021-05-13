K=int(input())
A,B=list(map(int,input().split()))

ans='OK'
if (A-0.1)//K == B//K :
    ans='NG'
    
print(ans)