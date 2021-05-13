a,b = map(int,input().split())
ans = abs(abs(a)-abs(b))
if a*b<0:ans+=1
if b<a<0 or 0<b<a:ans+=2
if a==0 and b<0:ans+=1
if b==0 and 0<a:ans+=1
print(ans)