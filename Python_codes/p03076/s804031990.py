l = [int(input()) for i in range(5)]
a = min(l, key=lambda x: (x-1)%10)
ret = 0
flag = 0
for i in l:
    if i != a or flag == 1:
        ret += i
    else:
        flag = 1
        
    if ret%10 != 0:
        ret += 10-(ret%10)
ret += a
print(ret)