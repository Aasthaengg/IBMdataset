x,y,a,b,c=map(int,input().split())
p=sorted(list(map(int,input().split())))[-x:]
q=sorted(list(map(int,input().split())))[-y:]
r=sorted(list(map(int,input().split())))
print(sum(sorted(p+q+r)[-x-y:]))