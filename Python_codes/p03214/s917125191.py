n=int(input())
a=list(map(int,input().split()))

ave=sum(a)/len(a)
a=list(map(lambda x:abs(x-ave), a))
min=sorted(a)[0]
print(a.index(min))