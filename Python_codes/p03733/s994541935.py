import sys
n,t = map(int,input().split())
li = list(map(int,input().split()))
count = t
if n == 1:
    print(t)
    sys.exit()
for i,l in enumerate(li):
    if i == 0:
        continue
    if l - li[i-1] <= t:
        count += l - li[i-1]
    else:
        count += t
print(count)