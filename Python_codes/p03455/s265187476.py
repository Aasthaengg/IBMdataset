from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
a,b = [tmp.pop(0) for _ in range(2)]

if a*b%2:   print('Odd')
else:   print('Even')