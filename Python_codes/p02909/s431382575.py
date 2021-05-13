import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

S = rs()

t2i = {'Sunny':0, 'Cloudy':1, 'Rainy':2}
i2t = ['Sunny', 'Cloudy', 'Rainy']

i = (t2i[S]+1)%3
print(i2t[i])
