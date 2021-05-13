n = int(input())
a = list(map(int, input().split()))

prev = a[0]
mon = 1000
stc = 0

for i in range(1, n):
    #print(prev)
    if prev < a[i]:
        stc = mon // prev
        mon = mon - stc * prev
        mon = stc * a[i] + mon
        #print("stc = {} mon = {}" .format(stc, mon))
    elif prev >= a [i]:
        pass
        #print("stc = {} mon = {}" .format(stc, mon))
    prev = a[i]

#mon = mon + stc * a[n - 1]

print(mon)