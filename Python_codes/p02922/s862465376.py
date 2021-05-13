a,b=list(map(int,input().split()))
if (b-1)%(a-1)==0:
    print(int((b-1)/(a-1)))
else:
    print(int((b-1)/(a-1))+1)
