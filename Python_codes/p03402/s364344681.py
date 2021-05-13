WHITE = '.'
BLACK = '#'

A, B = list(map(int, input().split()))

remain_white = A-1
remain_black = B-1

print("100 100")
for i in range(25):
    print(BLACK*100)
    if remain_white >= 50:
        print((WHITE+BLACK)*50)
        remain_white -= 50
    else:
        print((WHITE+BLACK)*remain_white + BLACK*(100-remain_white*2))
        remain_white = 0

for i in range(25):
    print(WHITE*100)
    if remain_black >= 50:
        print((WHITE+BLACK)*50)
        remain_black -= 50
    else:
        print((WHITE+BLACK)*remain_black + WHITE*(100-remain_black*2))
        remain_black = 0