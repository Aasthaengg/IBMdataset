n=int(input())
tv=1
av=1
for i in range(n):
    ti,ai=map(int,input().split())
    m=max(int((tv-1)//ti)+1,int((av-1)//ai)+1)
    tv=m*ti
    av=m*ai
print(tv+av)
