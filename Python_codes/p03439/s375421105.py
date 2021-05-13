N = int(input())
print(N-1, flush=True)
x = input()
if x == 'Vacant':
    exit(0)
print(0, flush=True)
s = input()
if s == 'Vacant':
    exit(0)
left = 0
right = N-1
mid = (right+left)//2
while True:
    print(mid, flush=True)
    t = input()
    if t == 'Vacant':
        exit(0)
    if bool(s == t) ^ bool((mid-left) % 2 == 0):
        right = mid
    else:
        left = mid
        s = t
    mid = (left+right)//2
