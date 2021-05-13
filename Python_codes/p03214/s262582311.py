n=int(input())
a=list(map(int,input().split(" ")))
ave=sum(a)/n
d=[]
for i in a:
    d.append(abs(i-ave))
print(d.index(min(d)))