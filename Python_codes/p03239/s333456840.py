n,T=map(int,input().split())
num=[]
for i in range(n):
    c,t=map(int,input().split())
    if t<=T:
        num.append(c)
if len(num)==0:
    print("TLE")
else:
    print(min(num))
