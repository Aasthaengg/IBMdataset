s = int(input())
if s == 1 or s == 2:
    print(4)
    exit(0)
cnt = 1
while(1):
    cnt += 1
    #print(s)
    if s == 1:
        break
    elif s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
print(cnt)