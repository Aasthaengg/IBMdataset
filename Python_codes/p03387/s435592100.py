X=list(map(int,input().split()))
if (max(X)*3)%2==sum(X)%2:
    print(int((max(X)*3-sum(X))/2))
else:
    print(int(((max(X)+1)*3-sum(X))/2))