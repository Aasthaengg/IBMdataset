sa = input()
sb = input()
sc = input()

tmp_a = 0
tmp_b = 0
tmp_c = 0

turn = 'a'

for _ in range(300):
    if turn == 'a':
        if tmp_a == len(sa):
            print('A')
            exit()
        turn = sa[tmp_a]
        tmp_a += 1
    if turn == 'b':
        if tmp_b == len(sb):
            print('B')
            exit()
        turn = sb[tmp_b]
        tmp_b += 1
    if turn == 'c':
        if tmp_c == len(sc):
            print('C')
            exit()
        turn = sc[tmp_c]
        tmp_c += 1