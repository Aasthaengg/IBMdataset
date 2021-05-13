n = int(input())
aaa = list(map(int, input().split(' ')))

ans = 0
mmm = int(1e9 + 7)
#for i in range(n):  # 1e5 ^ 2 なので...
#    for j in range(i+1, n):
#        ans = (ans + (aaa[i] ^ aaa[j])) % mmm

# 日本語的には自分より後ろのもの全部と xor を取った和

# 1 1 2 3 4 => 34
# 0 0 1
# 0 0 1
# 0 1 0 
# 0 1 1
# 1 0 0
#=======
# 4 2 1
#
# 4 * (4*1) + 2 * (3*2) * 1 * (2*3) = 34 (sum(ケタ * (0の数*1の数)) で合ってるっぽい?)
def get_bit_array(num):
    res = []
    while num > 0:
        res.append(num%2)
        num //= 2
    return res

bits = {}  # n がいくつあるか (n=1,2,4,8,...)
for i in range(n):
    t = aaa[i]
    bit_array = get_bit_array(t)
    r = 1
    for i in range(len(bit_array)):  # TLEかも
        bits[r] = bits.get(r, 0) + bit_array[i]
        r *= 2

# print(bits, n)
ans = 0
for k, v in bits.items():
    ans = (ans + k * (v * (n-v))) % mmm

print(ans)
