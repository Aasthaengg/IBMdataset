n = int(input())
s = input()
cnt = 0

for N in range(1000):
    tgt = str(N).zfill(3)
    if tgt[0] in s:
        i = s.index(tgt[0])
        if tgt[1] in s[i+1:]:
            j = s[i+1:].index(tgt[1]) + i
            if tgt[2] in s[j+2:]:
                cnt += 1
print(cnt)
