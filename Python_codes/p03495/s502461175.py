from collections import Counter
N, K = map(int, input().split())
A = [int(x) for x in input().split()]
c = Counter(A)
diff = len(c.keys()) - K
if diff<=0:
    print(0)
else:
    c_s = sorted(c.items(), key=lambda x: x[1])
    cnt=0
    for _, value in c_s:
        cnt += value
        diff -= 1
        if diff==0:
            break
    print(cnt)
        

