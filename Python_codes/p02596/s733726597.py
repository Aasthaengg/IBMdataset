k = int(input())
a = [7 % k]
if 7 % k == 0:
    print(1)
    exit()
for i in range(1,k):
    tmp = (a[-1] * 10 +7) % k
    if tmp == 0:
        print(i+1)
        exit()
    else:
        a.append(tmp)
print('-1')