sx,sy,tx,ty=map(int,input().split())
height=ty-sy
width=tx-sx
ans=""
ans+='U'*height+'R'*width+'D'*height+'L'*width
ans+='L'+'U'*(height+1)+'R'*(width+1)+'D'
ans+='R'+'D'*(height+1)+'L'*(width+1)+'U'
print(ans)
