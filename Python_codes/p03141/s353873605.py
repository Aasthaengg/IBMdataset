n=int(input())
AB=[]
B=[]
for _ in range(n):
    a,b=map(int,input().split())
    AB.append(a+b)
    B.append(b)
AB=sorted(AB,reverse=True)
#print(AB)
X=-sum(B)
for i in range(0,n,2):
    X+=AB[i]
print(X)