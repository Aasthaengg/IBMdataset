l=list(map(int,input().split()))
print(max(l)+max(max(l)-1,min(l)))