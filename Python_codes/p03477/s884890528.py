l =list(map(int,input().split()));a=sum(l[:2])-sum(l[2:]);print('Left') if a>0 else print('Right')if a<0 else print('Balanced')
