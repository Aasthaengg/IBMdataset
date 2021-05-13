n,a,b = map(int,input().split())
print(min(a,b),(0 if n>=a+b else (a+b)-n))