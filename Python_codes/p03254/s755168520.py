n, x = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
count = 0
for i in a:
    if x - i >= 0:
        x -= i
        count += 1
    else:
        break
if x != 0:
    count -= 1 if count == n else 0
print(count)