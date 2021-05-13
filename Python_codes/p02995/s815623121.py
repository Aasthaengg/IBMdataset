def main():
    import math
    a, b, c, d = map(int, input().split())

#a-bの間の数字の個数（"全体の個数"）を数える
    kosuu = b - a + 1
    
#c, d, c&dの最小公倍数と、a, bそれぞれの割り算の商を求めておく
    a_c = a // c
    a_d = a // d 
    b_c = b // c
    b_d = b // d
    
    lcm_cd = int(c// math.gcd(c,d) * d)
    a_cd = int(a // lcm_cd)
    b_cd = int(b // lcm_cd)

#c, d, c&dの最小公倍数がa, bの間に何個あるか（"約数の個数"）を数える（aは「a以上」の条件から検討に入れるべき数字のため、aで割り切れる場合は約数の個数として含める）
    if a % c == 0:
        kosuu_c = b_c - a_c + 1
    else:
        kosuu_c = b_c - a_c
    
    if a % d == 0:
        kosuu_d = b_d - a_d + 1
    else:
        kosuu_d = b_d - a_d

    if a % lcm_cd == 0:
        kosuu_cd = b_cd - a_cd + 1
    else:
        kosuu_cd = b_cd - a_cd

#全体の個数から約数の個数を引く。公倍数の約数の個数分多く引きすぎているため、足し戻す
    print(kosuu - kosuu_c - kosuu_d +kosuu_cd)




if __name__ == "__main__":
    main()
