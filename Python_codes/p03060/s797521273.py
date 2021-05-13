n=int(input())
v=[*map(int,input().split())]
c=[*map(int,input().split())]
print(sum(max(x-y,0) for x,y in zip(v,c)))