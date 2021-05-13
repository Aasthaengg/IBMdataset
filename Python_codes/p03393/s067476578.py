#print([chr(ord('a') + i) for i in range(26)])
#print([chr(i) for i in range(97, 97+26)])
import sys
import bisect
li = [chr(i) for i in range(97, 97+26)]
s = input()
if len(s)<26:
    for l in li:
        if l not in s:
            print(s+l)
            sys.exit()
elif s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
else:
    r = s[::-1]
    tmp = ''
    kabe = ''
    for i,rr in enumerate(r):
        if i == 0:
            continue
        if rr < r[i-1]:
            tmp = r[:i+1][::-1]
            kabe = rr
            break
    #print(tmp) #wzyx

    tmp_li = list(tmp)
    tmp_li.sort()
    ind = bisect.bisect_left(tmp_li, kabe)
    s0 = tmp_li[ind+1]
    #s0 = tmp_li[1]
    print(s.replace(tmp, s0))

    #print(tmp_li)
    #print(s - tmp + tmp[-1])
    #xx = list(tmp[1:])
    #xx.sort()
    #print(s[:26-len(tmp)] + xx[0])