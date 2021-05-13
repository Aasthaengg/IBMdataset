n,T=map(int,input().split())
la=[]
for i in range(n):
    c,t=map(int,input().split())
    if t<=T:la+=[(c,t)]
la=sorted(la,key=lambda x:x[0])
print("TLE" if la ==[] else la[0][0])