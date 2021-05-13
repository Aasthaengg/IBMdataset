import sys
def I(): return int(sys.stdin.readline().rstrip())

X = [I() for i in range(5)]
Y = [x % 10 for x in X if x % 10 != 0]
ans = sum(10*((x-1)//10+1) for x in X)

if len(Y) == 0:
    print(ans)
else:
    print(ans-10+min(Y))
