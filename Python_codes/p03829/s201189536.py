n, a, b = map(int, input().split())
x = list(map(int, input().split()))

if a >= b:
    thres = 0
else:
    thres = b // a

sub = []
for i in range(n-1):
    tmp = x[i+1] - x[i]
    sub.append(tmp)

count = 0
for i in range(n-1):
    if sub[i] <= thres:
        count += sub[i] * a
    else:
        count += b
print(count)