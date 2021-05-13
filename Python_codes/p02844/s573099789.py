# D - Lucky PIN
N = int(input())
S = input()

cnt = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            a = S.find(str(i))
            if a == -1:
                continue
            b = S.find(str(j),a+1)
            if b == -1:
                continue
            c = S.find(str(k),b+1)
            if c == -1:
                continue
            cnt += 1
print(cnt)