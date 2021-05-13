import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

SA,SB,SC = LS2(),LS2(),LS2()
a,b,c = 0,0,0
turn = 'a'
while a <= len(SA) and b <= len(SB) and c <= len(SC):
    if turn == 'a':
        if a == len(SA):
            print('A')
            break
        else:
            turn = SA[a]
            a += 1
    elif turn == 'b':
        if b == len(SB):
            print('B')
            break
        else:
            turn = SB[b]
            b += 1
    else:
        if c == len(SC):
            print('C')
            break
        else:
            turn = SC[c]
            c += 1
