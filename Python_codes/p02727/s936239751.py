x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))

p.sort()
q.sort()


sin=p[a-x:]+q[b-y:]+r

sin.sort()

print(sum(sin[len(sin)-x-y:]))
