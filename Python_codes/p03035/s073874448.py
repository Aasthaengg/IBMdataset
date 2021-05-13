from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))
tmp = LI()
a,b = [tmp.pop(0) for _ in range(2)]

if 13<=a:
    print(b)
elif 6<=a:
    print(int(b/2))
else:
    print(0)