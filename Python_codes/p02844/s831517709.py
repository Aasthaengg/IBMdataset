n = int(input())
s = input()

cnt = 0
for i in range(1000):
    si = str(i).zfill(3)
    k = 0
    for cn in range(n):
        if s[cn] == si[k]:
            if k == 2:
                cnt += 1
                break
            else:
                k += 1
print(cnt)