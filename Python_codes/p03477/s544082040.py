a,b,c,d=map(int,input().split())
print('Balanced') if a+b==c+d else print(['Left','Right'][a+b<c+d])