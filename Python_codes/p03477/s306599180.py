a,b,c,d = map(int,input().split())
a+=b
c+=d
print('Balanced' if a==c else ('Left' if a>c else 'Right'))