from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
r,d,x = [tmp.pop(0) for _ in range(3)]

for i in range(1,11):
    x = r*x-d
    print(x)