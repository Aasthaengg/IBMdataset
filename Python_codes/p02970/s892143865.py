n, k = map(int,input().split())
s, count = 1 + k, 0
while(True):
    if n-s > k:
        s += (2*k) + 1
        count += 1
    else:
        count += 1
        break
print(count)