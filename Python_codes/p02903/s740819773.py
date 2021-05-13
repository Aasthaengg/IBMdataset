h,w,a,b=map(int,input().split())
A=[]
for i in range(b):
    A.append(["1"]*a+["0"]*(w-a))
for i in range(h-b):
    A.append(["0"]*a+["1"]*(w-a))
for l in A:
    print("".join(l))