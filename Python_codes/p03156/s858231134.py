n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
li1 = [i for i in p if i<=a]
li2 = [i for i in p if a<i<=b]
li3 = [i for i in p if b<i]
a,b,c=len(li1),len(li2),len(li3)
print(min(a,b,c))