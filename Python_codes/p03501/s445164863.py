n,a,b = map(int,input().split())
print(b if a*n>b else a*n if a*n<b else a*n)