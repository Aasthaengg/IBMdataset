S = int(input())
p = 10 ** 9
if S > p:
    r = S % p
    r = 0 if r == 0 else p - r 
    print(p, 1, r, (S + r) // p,  0, 0)
else:
    print(1, 0, 0, S, 0, 0)