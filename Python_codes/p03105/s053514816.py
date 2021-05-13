A,B,C=list(map(int,input().split()))

if A*C <= B:
    ans = C
else:
    ans = B//A
    
print(ans)