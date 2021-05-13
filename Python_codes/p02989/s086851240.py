N = int(input())
d = list(map(int,input().split()))
A = N//2
d.sort()
if d[A-1]==d[A]:
    print("0")
else:
    print(d[A]-d[A-1])