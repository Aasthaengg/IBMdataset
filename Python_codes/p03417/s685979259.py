def main():
    B = input()
    B = B.split()
    B = [int(i) for i in B]
    n = B[0]
    m = B[1]
    if m * n == 0:
        return 0
    if min(n, m) == 1:
        if max(n, m) == 1:
            return 1
        else:
            return max(n, m) - 2
    else:
        nc = n - 2
        mc = m - 2
        return nc * mc
          
print(main())