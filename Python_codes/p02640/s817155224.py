x,y=map(int,input().split())
print('YNeos'[y&1 or x*2>y or y>x*4::2])