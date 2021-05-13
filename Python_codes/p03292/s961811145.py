p,q,r=map(int,input().split())
print(min([abs(p-q)+abs(q-r),abs(q-r)+abs(p-r),abs(p-q)+abs(p-r)]))