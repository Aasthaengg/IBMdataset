sx,sy,tx,ty=map(int,input().split())
print('U'*(ty-sy)+'R'*(tx-sx)+'D'*(ty-sy)+'L'*(tx-sx)+'L' \
      +'U'*(ty+1-sy)+'R'*(tx+1-sx)+'D'+'R'+'D'*(ty+1-sy) \
      +'L'*(tx+1-sx)+'U')