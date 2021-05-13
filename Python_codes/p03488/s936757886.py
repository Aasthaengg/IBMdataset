s = input()
x,y = map(int,input().split())

move = [0]
for si in s:
    if(si  == 'F'):
        move[-1] += 1
    else:
        move.append(0)

move_x = move[2::2]
move_y = move[1::2]
for a,move_a in zip([x-move[0],y],[move_x,move_y]):
    m_max = sum(move_a)
    if(m_max < abs(a)):
        print('No')
        exit()

    dp = 2**m_max
    for mi in move_a:
        dp = (dp<<mi) | (dp>>mi)

    if(dp >> (m_max+a))&1:
        continue
    else:
        print('No')
        exit()

print('Yes')