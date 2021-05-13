S = input()

max_len = 0
for i in range(10):
    for j in range(i, 10):
        s = S[i:j+1]
        for n, k in enumerate(s, 1):
            if k not in ['A', 'T', 'G', 'C']:
                break
            if n == len(s):
                max_len = max(max_len, len(s))
print(max_len)