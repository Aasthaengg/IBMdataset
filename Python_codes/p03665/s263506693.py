import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
num_pack, mod = map(int,input().split())
pack_ls = list(map(int, input().split()))
num_pack_0 = 0
num_pack_1 = 0
for i in range(num_pack):
    if pack_ls[i] % 2 == 0:
        num_pack_0 += 1
    else:
        num_pack_1 += 1

if mod == 1:
    pattern_0 = 2 ** num_pack_0
    pattern_1 = 0
    i = 1
    while i <= num_pack_1:
        pattern_1 += combinations_count(num_pack_1, i)
        i += 2
    ans = pattern_0 * pattern_1
else:
    pattern_0 = 2 ** num_pack_0
    pattern_1 = 0
    i = 0
    while i <= num_pack_1:
        pattern_1 += combinations_count(num_pack_1, i)
        i += 2
    ans = pattern_0 * pattern_1

print(ans)
    





