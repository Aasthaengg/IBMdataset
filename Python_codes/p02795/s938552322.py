#A
h = int(input())
w = int(input())
n = int(input())

cnt = 0
flg = True
if h > w:
    while flg:
        if h * cnt >= n:
            flg = False
            break
        cnt += 1
        
else:
    while flg:
        if w * cnt >= n:
            flg = False
            break
        cnt += 1
        
print(cnt)