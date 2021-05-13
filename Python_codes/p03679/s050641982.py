x,a,b=map(int,input().split())
 
print('delicious'if b<=a else 'safe' if a<b and b-a<=x else 'dangerous')