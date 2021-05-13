n=int(input())
l=list(map(int,input().split()))
l=sorted([x-i-1 for i,x in enumerate(l)])
x=l[n//2]
print(sum([abs(i-x) for i in l]))