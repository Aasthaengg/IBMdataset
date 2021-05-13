N, K = [int(i) for i in input().split()]
R,S,P = [int(i) for i in input().split()]
T = input()

def wincard(s):
    if s=="r":
        return "p"
    elif s=="s":
        return "r"
    else:
        return "s"

def score(card):
    if card == "r":
        return R
    elif card == "s":
        return S
    elif card == "p":
        return P

mycard = ""
score_sum = 0
for i in range(N):
    if i-K<0:
        mycard = mycard+wincard(T[i])
        score_sum += score(wincard(T[i]))
    else:
        if wincard(T[i]) != mycard[i-K]:
            mycard = mycard+wincard(T[i])
            score_sum += score(wincard(T[i]))
        else:
            mycard = mycard+"w"

print(score_sum)