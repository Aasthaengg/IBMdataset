s,t=input().split()
a,b=map(int,input().split())
u=input()
if s==u:
    print(int(a-1),int(b))
else:
    print(int(a),int(b-1))