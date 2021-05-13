from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
a,p = [tmp.pop(0) for _ in range(2)]
ans = int((3*a+p)/2)
print(ans)