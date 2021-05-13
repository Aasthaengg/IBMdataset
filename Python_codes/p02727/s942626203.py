x,y,a,b,c = map(int,input().split())
p = sorted(list(map(int,input().split())),reverse=True)[:x]
q = sorted(list(map(int,input().split())),reverse=True)[:y]
r = list(map(int,input().split()))
print(sum(sorted(p+q+r,reverse=True)[:(x+y)]))