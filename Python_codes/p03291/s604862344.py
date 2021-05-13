S = input()
mod = 10 ** 9 + 7

a = b = ans = 0
a_old = b_old = ans_old = 0

q = 1 
for s in S:
    if s == "A":
        a = (a_old + q) % mod
        b = b_old
        ans = ans_old
    elif s == "B":
        a = a_old
        b = (b_old + a_old) % mod
        ans = ans_old
    elif s == "C":
        a = a_old
        b = b_old
        ans = (ans_old + b_old) % mod
    else:
        a = (3 * a_old + q) % mod
        b = (3 * b_old + a_old) % mod
        ans = (3 * ans_old + b_old) % mod
        q = q * 3 % mod
    a_old = a
    b_old = b
    ans_old = ans
    # print(a, b, ans)

print(ans)
