S = input()

MOD = 1000000007

# a_b_c, a_b_hc, a_hb_c, a_hb_hc, ha_b_c, ha_b_hc, ha_hb_c, ha_hb_hc
count = [[0, 0, 0] for _ in range(8)]
hatena_count = 0

for c in S:
    if c == 'A':
        nums = [0,1,2,3]
        for num in nums:
            count[num][0] += 1
    elif c == 'B':
        nums = [0,1,4,5]
        for num in nums:
            count[num][1] += count[num][0]
    elif c == 'C':
        nums = [0,2,4,6]
        for num in nums:
            count[num][2] += count[num][1]
    elif c == '?':
        # hc
        nums = [1,3,5,7]
        for num in nums:
            count[num][2] += count[num][1]
        
        # hb
        nums = [2,3,6,7]
        for num in nums:
            count[num][1] += count[num][0]

        # ha
        nums = [4,5,6,7]
        for num in nums:
            count[num][0] += 1
        
        hatena_count += 1

total = 0
coef = [0, 1, 1, 2, 1, 2, 2, 3]
for i in range(8):
    total += count[i][2] * 3**(hatena_count - coef[i])

print(int(total % MOD))