SX,SY,TX,TY=map(int,input().split())

dt={'U':'D','D':'U','L':'R','R':'L'}

def f(s):
    t=''
    for a in s:
        t+=dt[a]
    return t

vx=TX-SX
vy=TY-SY

ans1=''
ans1=('U' if 0<=vy else 'D')*abs(vy)
ans1+=('R' if 0<=vx else 'L')*abs(vx)
ans1+=f(ans1)

ans2=''
ans2=('R' if 0<=-vx else 'L')
ans2+=('U' if 0<=vy else 'D')*abs(vy+1)
ans2+=('R' if 0<=vx else 'L')*abs(vx+1)
ans2+=('U' if 0<=-vy else 'D')
ans2+=f(ans2)
print(ans1+ans2)
