#template
def inputlist(): return [int(k) for k in input().split()]
#template
X,Y = inputlist()
if X % Y == 0:
    print(-1)
else:
    print(X)