a,b,c = map(int,input().split())
n1,n2,n3 = sorted([a,b,c],reverse= True)

print(10*n1 + n2 + n3)