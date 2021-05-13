import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

li = [a,b,c,d,e]

ma = 0
s = 0
for i in li:
    tmp = ((i + (10 - 1)) // 10) * 10
    s += tmp
    ma = max(ma, abs(i - tmp))

print(s - ma)
