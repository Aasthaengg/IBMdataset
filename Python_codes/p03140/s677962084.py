n=int(input())
a=input()
b=input()
c=input()
x=[[a[i],b[i],c[i]] for i in range(n)]
y=[max([t.count(t[0]),t.count(t[1]),t.count(t[2])]) for t in x]
print(3*n-sum(y))