N = int(input())
s  = input().strip()

cnt = 0
for key in range(1000):
    key = '{:0>3}'.format(str(key))    #; print(key)
    i0 = s.find(key[0])
    if 0 <= i0 < N-2:
        i1 = s.find(key[1], i0+1)
        if 0 < i1 < N-1:
            i2 = s.find(key[2], i1+1)
            if i2 != -1:
                cnt += 1                                 
print(cnt)      