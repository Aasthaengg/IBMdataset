N = int(input())
S = input()

def pop_cnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c

pop_S = 0
for s in S:
    if s == "1":
        pop_S += 1

p1 = pop_S + 1
p2 = pop_S - 1
#print(p1, p2)

mod_sum1 = 0
mod_sum2 = 0
for i, s in enumerate(S):
    if s == "1":
        mod_sum1 = (mod_sum1 + pow(2, N - i - 1, p1)) % p1
        if p2:
            mod_sum2 = (mod_sum2 + pow(2, N - i - 1, p2)) % p2
#print(mod_sum1, mod_sum2)

cnt = [0] * (p1 + 2)

for i in range(1, p1 + 1):
    cnt[i] = cnt[i % pop_cnt(i)] + 1
#print(cnt)

for i, s in enumerate(S):
    if s == "0":
        mod_sum = (mod_sum1 + pow(2, N - i - 1, p1)) % p1
        #print(mod_sum)
        print(cnt[mod_sum] + 1)
    else:
        if pop_S == 1:
            print(0)
        else:
            mod_sum = (mod_sum2 - pow(2, N - i - 1, p2)) % p2
            #print(mod_sum)
            print(cnt[mod_sum] + 1)
