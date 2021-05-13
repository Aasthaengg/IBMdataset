h = int(input())
w = int(input())
n = int(input())

q,r = divmod(n, max(h,w))
print(q + int(bool(r)))