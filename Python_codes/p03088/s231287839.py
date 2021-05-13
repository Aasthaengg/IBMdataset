from collections import defaultdict as dd
n = int(input())
ng = set(["AGC", "GAC", "ACG", "AGGC", "ACGC", "ATGC", "AGAC", "AGGC", "AGTC"])
#moji_count[str] => num_of_moji
moji_count = dd()
moji_count[""] = 1
cand = ["A", "G", "C", "T"]
mod = 10**9 + 7

for i in range(n):
    temp = dd(int)
    for base_moji, num_moji in moji_count.items():
        if len(base_moji) >= 4:
            base_moji = base_moji[1:]
        for add_moji in cand:
            new_moji = base_moji + add_moji
            for ng_word in ng:
                if ng_word in new_moji:
                    break
            else:
                temp[new_moji] += num_moji % mod
        moji_count = temp

print(sum(moji_count.values()) % mod)