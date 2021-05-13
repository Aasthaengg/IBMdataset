n,m = map(int,input().split())
lr = [list(map(int,input().split()))for i in range(m)]

low = 1
high = 10**5

for l,r in lr:
    if low <= l:
        low = l 
    if r <= high:
        high = r 

if high < low:
    print(0)
    exit()
print(high - low + 1)