x,a,b=map(int,input().split())
print('delicious' if 0>=b-a else 'safe' if x>=b-a else 'dangerous')