A,B=map(int,input().split())
l=[]
l=[A+B,A-B,A*B]
l.sort(reverse=True)

print(l[0])