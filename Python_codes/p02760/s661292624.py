def bingo_judge(li,a,b,c,d,e,f,flag):
    if li[a-1][b-1] + li[c-1][d-1] + li[e-1][f-1] == 3:
        return True
    if flag:
        return True
    else:
        return False

card = []
card_judge = []
for i in range(3):
    li = list(map(int, input().split()))
    card.append(li)
    card_judge.append([0,0,0])
N = int(input())
for i in range(N):
    number = int(input())
    for t in range(3):
        for u in range(3):
            if number == card[t][u]:
                card_judge[t][u] = 1
flag = False
flag = bingo_judge(card_judge,1,1,2,1,3,1,flag)
flag = bingo_judge(card_judge,1,2,2,2,3,2,flag)
flag = bingo_judge(card_judge,1,3,2,3,3,3,flag)
flag = bingo_judge(card_judge,1,1,1,2,1,3,flag)
flag = bingo_judge(card_judge,2,1,2,2,2,3,flag)
flag = bingo_judge(card_judge,3,1,3,2,3,3,flag)
flag = bingo_judge(card_judge,1,1,2,2,3,3,flag)
flag = bingo_judge(card_judge,1,3,2,2,3,1,flag)
if flag:
    print('Yes')
else:
    print('No')