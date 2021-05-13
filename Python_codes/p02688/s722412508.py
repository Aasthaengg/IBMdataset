n,k=map(int,input().split());a=set()
for i in range(k):d=input();a|=set(list(map(int,input().split())))
print(n-len(a))