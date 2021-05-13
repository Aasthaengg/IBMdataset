import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
l = [ai for ai in a[:-1]]
l.sort(key=lambda x: abs(a[-1]/2-x))
print(a[-1], l[0])