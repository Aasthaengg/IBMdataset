import numpy as np

n, k = map(int, input().split())

value = np.array(list(map(int, input().split())))
r_value = value[::-1]

max_value = max(value[0], r_value[0])
for i in range(1, k):
    total_value = 0
    if i > n:
        s = value
        s.sort()
        s = list(s)
        for j in range(k-n):
            if s[0] < 0:
                s.pop(0)
        total_value = sum(s)
    else:
        for j in range(i+1):
            a = value[0:j]
            b = r_value[0:i-j]
            c = np.concatenate((a, b))
            c.sort()
            c = list(c)
            for l in range(k-i):
                if c[0] < 0:
                    c.pop(0)
                if c == []:
                    break
            total_value = sum(c)
            if total_value > max_value:
                max_value = total_value
print(max_value)