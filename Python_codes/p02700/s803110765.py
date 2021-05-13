a, b, c, d = map(int, input().split())

while a or c > 0:
        aoki_hitpoint = c - b
        if aoki_hitpoint <= 0:
            c = 0
            print('Yes')
            exit()
        else:
            c = aoki_hitpoint

        takahash_hitpoint = a - d
        if takahash_hitpoint <= 0:
            a = 0
            print('No')
            exit()
        else:
            a = takahash_hitpoint
