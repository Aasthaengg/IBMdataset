N = int(input())
B = input()

B_1 = B.count("1") # pc
mod_p1 = int(B, 2) % (B_1 + 1) # pc + 1
if B_1 != 1:
    mod_m1 = int(B, 2) % (B_1 - 1) # pc - 1

# 小さい数字は直接計算しても一瞬
def calc_small(n, count):
    count += 1
    mod = n % bin(n).count("1")
    if mod == 0:
        return count
    else:
        return calc_small(mod, count)

for i in range(N):
    if B_1 == 1 and int(B[i]) == 1:
        print(0)
        continue

    # はBiが1か0かで，元のmodから差分計算できる
    if B[i] == '1':
        # 反転して-する場合 (mod PC - 1)
        mod = (mod_m1 - pow(2, N - i - 1, B_1 - 1)) % (B_1 - 1)
    else:
        # 反転して+する場合 (mod PC + 1)
        mod = (mod_p1 + pow(2, N - i - 1, B_1 + 1)) % (B_1 + 1)
    count = 1
    if mod == 0:
        print(count)
    else:
        print(calc_small(mod, count))
