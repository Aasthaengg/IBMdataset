h = int(input())
w = int(input())
n = int(input())
if h >= w:
    _max = h
    _min = w
else:
    _max = w
    _min = h
for i in range(1, _min+1):
    if _max * i >= n:
        print(i)
        break
