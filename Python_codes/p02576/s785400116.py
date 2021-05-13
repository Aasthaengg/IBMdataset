n, x, t = map(int, input().split())
if n%x == 0:
    kosuu = n/x
else:
    kosuu = n/x+1
print(int(kosuu)*t)