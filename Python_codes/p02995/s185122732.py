from fractions import gcd #最大公約数
A, B, C, D = map(int, input().split())
# (0~Bのうち, C,D,C*Dの倍数ではないものの数)　- (0~-Aのうち, C,D,C*Dの倍数ではないものの数)
lcm = C * D // gcd(C, D) #C,Dの最小公倍数
x = (A - 1) - (A - 1) // C - (A - 1) // D + (A - 1) // lcm
y = B - B // C - B // D + B // lcm
# (0~Bの数) - {(0~BのうちCで割り切れる数) + (0~BのうちDで割り切れる数) - (0~BのうちC,Dの最小公倍数で割り切れる数)}
print(y - x)