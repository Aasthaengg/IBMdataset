a,b,c=map(int,input().split())
print(["A","B"][abs(b-a)>abs(c-a)])