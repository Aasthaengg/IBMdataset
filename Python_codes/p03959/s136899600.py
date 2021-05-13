n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mt_t=[0]*n
mt_a=[0]*n
last=0
for i in range(len(t)):
    if last < t[i]:
        mt_t[i] = -t[i]
        last=t[i]
    else:
        mt_t[i] = last
last=0
for i in reversed(range(len(t))):
    if last < a[i]:
        mt_a[i] = -a[i]
        last=a[i]
    else:
        mt_a[i] = last
mts = [0]*n
for i in range(len(t)):
    if mt_t[i] < 0 and mt_a[i] < 0:
        if mt_t[i] != mt_a[i]:
            print(0)
            exit()
    elif mt_t[i] < 0 or mt_a[i] < 0:
        kaku =abs(min(mt_t[i],mt_a[i]))
        kouho=max(mt_t[i],mt_a[i])
        if kouho < kaku:
            print(0)
            exit()
    mts[i] = min(mt_t[i],mt_a[i])

ans=1
for num in mts:
    if num > 0:
        ans*=num
        ans%=(10**9+7)
print(ans)