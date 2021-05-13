n=int(input())
lst=sorted(map(int,input().split()))
m=lst[-1]/2
anslst=[]
for i in range(n-1):
    anslst.append([abs(m-lst[i]),lst[i]])
anslst.sort()
print(int(m*2),anslst[0][1])