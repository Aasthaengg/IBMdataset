n, x = map(int,input().split())
l = list(map(int, input().split()))
s = 0
count = 1
for i in l:
    s += i
    if s > x:
        break
    count += 1
print(count)
