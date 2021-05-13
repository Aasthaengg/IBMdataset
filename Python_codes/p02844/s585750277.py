import re
#import time
N = int(input())
S = input()
#start = time.time()
cnt = 0
for i in range(10):
    fir = S.find(str(i))
    if fir == -1:
        continue
    for j in range(10):
        sec = S.find(str(j), fir + 1)
        if sec == -1:
            continue
        for h in range(10):
            thi = S.find(str(h), sec + 1)
            if thi == -1:
                continue
            cnt += 1
print(cnt)
#stop = time.time()
#print(stop - start)