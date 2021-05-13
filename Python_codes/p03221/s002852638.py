from bisect import bisect_right
n,m=map(int,input().split())
p,y=[],[]
l={}
for i in range(m):
 p_,y_=map(int,input().split())
 p.append(p_)
 y.append(y_)
 if not p_ in l:l[p_] = []
 l[p_].append(y_)
for i in l:
 l[i].sort()
for i in range(m):
 print(str(p[i]).zfill(6)+str(bisect_right(l[p[i]],y[i])).zfill(6))