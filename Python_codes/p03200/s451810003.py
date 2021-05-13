#import random, string

#def randomname(n):
#    candidate_text = ["W","B"]
#    randlst = [random.choice(candidate_text) for i in range(n)] #()の中身を string.ascii_letters + string.digits とすると大小英数字
#    return ''.join(randlst)

S = [0] + list(input())
#S = [0] + list(randomname(2*10**5))

N = len(S) - 1

#頭のWは無視
i = 1
while 1:
    #print(i,S[i])

    if i == N:
        print(0)
        break
    elif S[i] == "W":
        i += 1
    else:
        #print("BW pattern")

        ans = 0
        start = i
        B_count = 1

        for j in range(start+1,N+1):
            if S[j] == "W":
                ans += B_count
            elif S[j] == "B":
                B_count += 1
        print(ans)
        break
