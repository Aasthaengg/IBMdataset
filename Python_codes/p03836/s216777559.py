import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a,b,c,d = MI()
x,y = c-a,d-b
ANS = ['R']*x + ['U']*y + ['L']*x + ['D']*(y+1) + ['R']*(x+1) + ['U']*(y+1) + ['L'] + ['U'] + ['L']*(x+1) + ['D']*(y+1) + ['R']
print(''.join(ANS))
