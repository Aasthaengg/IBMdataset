N = int(input())
S = input()
m = 10 ** 6
tot1 = 0
cnt1 = 0
cnt0 = 0
for s in S:
    if(s == '#'):
        cnt0 += 1
    else:
        cnt1 += 1
        tot1 += 1
    m = min(m,cnt0-cnt1)
m += tot1
m = min(m,tot1)
print(m)