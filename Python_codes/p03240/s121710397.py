N=int(input())
q=[list(map(int,input().split())) for _ in range(N)]
for i in range(101):
    for j in range(101):
        F=1
        r=[]
        for k in range(101):
            x,y,h=q[k]
            if h > 0:
              break
            r.append([x,y])
        s=h+abs(x-i)+abs(y-j)
        for x,y,h in q[1:]:
            if h==0:
                r.append([x,y])
                continue
            y=h+abs(x-i)+abs(y-j)
            if s!=y:
              F=0
              break
        if r:
          for x,y in r:
            if s-abs(x-i)-abs(y-j) > 0:
              F=0
              break
        if F==1:
          print(i,j,s)
          exit()