h = int(input())
w = int(input())
n = int(input())

r = max(h,w)
if n%r != 0:
    print(n//r + 1)
else:
    print(int(n/r))