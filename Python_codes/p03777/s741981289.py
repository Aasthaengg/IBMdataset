x,y=map(str,input().split())
if x == 'H':
    print(y)
elif x == 'D':
    print('H' if y=='D' else 'D')