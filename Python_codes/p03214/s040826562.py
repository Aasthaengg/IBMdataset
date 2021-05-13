n=int(input())
a=list(map(int,input().split()))
av=sum(a)/len(a)
b=[abs(i-av) for i in a]
print(b.index(min(b)))