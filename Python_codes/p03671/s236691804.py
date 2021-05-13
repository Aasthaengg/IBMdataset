a,b,c=map(int,input().split())
n=[a+b,a+c,b+c]
n.sort()
print(n[0])