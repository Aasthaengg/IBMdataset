s = input()
N = len(s)

# AABC->ABCA->BCAA
# ABCの前にAがn個->ABCの後にAがn個

# ABCABC->BCABCA->BCBCAA

# AかBCでない並びがあったら切断

# Aを右に BCを左に移動させる操作
# BCがあったら、それより左にあるAの数だけansが増える


i = 0
a = 0
ans = 0

while i < len(s):
    if s[i] == 'A':
        a += 1
        i += 1
        continue
    if s[i] == 'B' and i + 1 < N:
        if s[i + 1] == 'C':
            ans += a
            i += 2
            continue
    a = 0
    i += 1

print(ans)
