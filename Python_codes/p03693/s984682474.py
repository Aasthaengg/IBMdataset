a,b,c=map(int,input().split())
print('YNEOS'[(b*10+c)%4!=0::2])