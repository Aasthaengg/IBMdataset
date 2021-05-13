n = int(input())
seq = [[],[]]
seq[0] = input()
seq[1] = input()
i = 0

ans = 3
cnt_vert = 0
cnt_hor = 0
m = 1000000007
# print(seq)
while i < len(seq[0]):
    if seq[0][i] == seq[1][i]: # vert
        if cnt_vert == 0:
            mult = 1
        elif cnt_vert > 0:
            mult = 2
        else:
            raise ValueError("wtf?")
        cnt_vert += 1
        cnt_hor = 0

    else:
        if cnt_hor == 0:
            mult = 2
        elif cnt_hor > 0:
            mult = 3
        else:
            # print(i, cnt_hor, cnt_vert)
            raise ValueError("wtf hor")
        cnt_vert = 0
        cnt_hor += 1
        i += 1
    
    i += 1
    ans *= mult
    if ans > m:
        ans = ans % m
print(ans)