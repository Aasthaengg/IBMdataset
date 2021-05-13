import sys
lines = sys.stdin.readlines()
cnt = [0 for i in range(26)]
for line in lines:
    line = line.lower()
    alph = [chr(ord('a') + i) for i in range(26)]
    for idx, i in enumerate(alph):
        for k in line:
            if i == k:
                cnt[idx] += 1
for idx, i in enumerate(alph):
    print("{0} : {1}".format(i, cnt[idx]))
