S = input()
MOD = 10 ** 9 + 7

A = 0
AB = 0
ABC = 0
cnt = 1

for s in S:
    if s == "A":
        A = (A + cnt) % MOD
    elif s == "B":
        AB = (A + AB) % MOD
    elif s == "C":
        ABC = (AB + ABC) % MOD
    else:
        A, AB, ABC = (A * 3 + cnt) % MOD, (AB * 3 + A) % MOD, (ABC * 3 + AB) % MOD
        cnt = (cnt * 3) % MOD
    # print(A, AB, ABC, cnt)
    
print(ABC)