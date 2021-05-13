l=map(int,raw_input().split())
n=raw_input()
ans=chk=0


def rolling(word,dice):
    if word=='S':
        dice[0],dice[1],dice[5],dice[4]=dice[4],dice[0],dice[1],dice[5]
    elif word=='N':
        dice[0],dice[1],dice[5],dice[4]=dice[1],dice[5],dice[4],dice[0]
    elif word=='W':
        dice[0],dice[2],dice[5],dice[3]=dice[2],dice[5],dice[3],dice[0]
    else:
        dice[0],dice[2],dice[5],dice[3]=dice[3],dice[0],dice[2],dice[5]
    return dice

for i in n:
    l=rolling(i,l)
print l[0]