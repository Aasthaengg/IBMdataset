ax,ay,bx,by=map(int,input().split())


cx=bx+ay-by
cy=by+bx-ax
dx=ax+ay-by
dy=ay+bx-ax

print("{} {} {} {}".format(cx,cy,dx,dy))