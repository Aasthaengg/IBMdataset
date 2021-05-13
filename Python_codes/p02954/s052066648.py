S = input()

n = len(S)

l = [0]*n
current_run = 'R'
R_start = 0

for i in range(n-1):
    if current_run == 'R':
        if S[i+1] == 'L':
            R_len = i+1 - R_start
            current_run = 'L'
            L_start = i+1
            if i == n-2:
                placeR = L_start - 1
                placeL = L_start
                L_len = 1
                D_len = (R_len + L_len) // 2
                l[placeR] = D_len
                l[placeL] = D_len
                if (R_len + L_len) % 2 == 0:
                    continue
                if R_len > D_len:
                    if R_len % 2 == 0:
                        l[placeL] += 1
                    else:
                        l[placeR] += 1

    else:
        if S[i+1] == 'R' or i == n-2:
            L_len = i+1 - L_start
            if i == n-2: L_len += 1
            current_run = 'R'
            R_start = i+1
            placeR = L_start - 1
            placeL = L_start
            D_len = (R_len + L_len) // 2
            l[placeR] = D_len
            l[placeL] = D_len
            if (R_len + L_len) % 2 == 0:
                continue
            if R_len > D_len:
                if R_len % 2 == 0:
                    l[placeL] += 1
                else:
                    l[placeR] += 1
            elif L_len > D_len:
                if L_len % 2 == 0:
                    l[placeR] += 1
                else:
                    l[placeL] += 1

print(" ".join([str(_) for _ in l]))