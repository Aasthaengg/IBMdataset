import sys
import bisect
input=sys.stdin.readline
a,b,q=map(int,input().split())
s=[ int(input()) for _ in range(a)]
t=[ int(input()) for _ in range(b)]
#print(s,end=" s\n")
#print(t,end=" t\n")
for _ in range(q):
  x=int(input())
  sr=bisect.bisect_left(s,x)
  sr=sr-1 if sr==len(s) else sr
  sl=sr-1 if sr>0 else sr 
  tr=bisect.bisect_left(t,x)
  tr=tr-1 if tr==len(t) else tr
  tl=tr-1 if tr>0 else tr
 # print(sl,sr,tl,tr)
  def f(i,j):
    #print( abs(x-s[i]),abs(x-t[j]))
    return min(abs(x-s[i]),abs(x-t[j]))+abs(t[j]-s[i])
#  print(x)
#  print(f(sl,tl),f(sl,tr),f(sr,tl),f(sr,tr))
  ans=min(f(sl,tl),f(sl,tr),f(sr,tl),f(sr,tr))
  print(ans)



  


