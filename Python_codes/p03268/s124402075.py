n, k = map(int, input().split())
n_mod0 = n//k

if k % 2:
    print(n_mod0**3)
else:
    n_modk2 = (n+(k//2))//k
    print(n_mod0**3 + n_modk2**3)
