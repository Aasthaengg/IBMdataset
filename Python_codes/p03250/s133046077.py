a,b,c=map(int,input().split())
lst=[a,b,c]
lst=sorted(lst)
print(10*(lst[-1])+sum(lst[:2]))