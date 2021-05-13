n,a,b = map(int,input().split())

pair = n-2
print(max(pair*b-pair*a+1,0))