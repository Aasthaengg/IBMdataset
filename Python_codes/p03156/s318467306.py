n=int(input())
a,b,=map(int,input().split())
p=sorted(list(map(int,input().split())))
print(min(sum(i<=a for i in p),sum(a<i and i<=b for i in p),sum(b<i for i in p)))
