a,b,c,d = map(int,input().split())
sl = a + b
sr = c + d
if sl == sr: print('Balanced')
elif sl > sr: print('Left')
else: print('Right')