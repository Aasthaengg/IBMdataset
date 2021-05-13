import sys

cnt = [0]*26
for line in sys.stdin:
    for a in line:
        if(ord(a) >= 65 and ord(a) <= 90):
            cnt[ord(a) - 65] += 1
        if(ord(a) >= 97 and ord(a) <= 122):
            cnt[ord(a) - 97] += 1

for i in xrange(26):
    print unichr(97 + i) + " : " + str(cnt[i])