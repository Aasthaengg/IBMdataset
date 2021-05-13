n = list(map(int,input()))
cnt = 0
b = tuple(n)
c = b

for i in n:
    cnt += 1
    if i == 9:
        continue
    else:
        if cnt == len(n):
            cnt -= 1
            n[cnt-1] -= 1
            break
        else:
            if i == 0:
                n[cnt-2] -= 1
                cnt -= 1
                break
            else:
                n[cnt-1] -= 1
                break

for i in range(cnt,len(n)):
    n[i] = 9

if len(n) == 1:
    n = b

if sum(n) >= sum(b):
    print(sum(n))
else:
    print(sum(b))