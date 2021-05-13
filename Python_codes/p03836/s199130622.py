SX,SY,TX,TY=map(int,input().split())
dt={'U':'D','D':'U','L':'R','R':'L'}
def f(s):
 t=''
 for a in s:t+=dt[a]
 return t

vx=TX-SX
vy=TY-SY

ans1='U'*vy+'R'*vx
ans1+=f(ans1)
ans2='L'+'U'*(vy+1)+'R'*(vx+1)+'D'
ans2+=f(ans2)

print(ans1+ans2)