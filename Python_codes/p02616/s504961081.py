
N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 1000000007

zeros = []
pluss = []
minuss = []

for i in range(N):
    if A[i]>0:
        pluss.append(A[i])
    elif A[i]==0:
        zeros.append(A[i])
    else:
        minuss.append(A[i])

pluss = sorted(pluss, reverse = True)
minuss = sorted(minuss)

if len(pluss) + (min(len(minuss), K)//2)*2 >= K:
    answer_type = 1
elif len(zeros) > 0:
    answer_type = 2
else:
    answer_type = 3


rest = K
if answer_type == 1:
    plus_now = 0
    minus_now = 0
    minus_counter = 0
    answer = 1
    for i in range(K):
        if plus_now < len(pluss):
            plus_target = pluss[plus_now]
        else:
            plus_target = -1000000000000
        
        if minus_now < len(minuss):
            minus_target = -minuss[minus_now]
        else:
            minus_target = -1000000000000
        
        if plus_target >= minus_target:
            answer = (answer*plus_target)%mod
            plus_now += 1
        else:
            answer = (answer*minus_target)%mod
            minus_now += 1
            minus_counter += 1

    if minus_counter%2 == 1:
        #★インデックスの有効範囲をよく考えること、勝手に-1とかなっちゃう★
        if minus_now >= len(minuss) or plus_now == 0:
            answer = answer * pow(-minuss[minus_now-1],mod-2,mod)
            answer = (answer * pluss[plus_now])%mod
        elif plus_now >= len(pluss) or minus_now == 0:
            answer = answer * pow(pluss[plus_now-1],mod-2,mod)
            answer = (answer * -minuss[minus_now])%mod
        #★割り算の時は有効桁数よく考えること★
        elif pluss[plus_now]*pluss[plus_now-1] > -minuss[minus_now]*(-minuss[minus_now-1]):
            answer = answer * pow(-minuss[minus_now-1],mod-2,mod)
            answer = (answer * pluss[plus_now])%mod
        else:
            answer = answer * pow(pluss[plus_now-1],mod-2,mod)
            answer = (answer * -minuss[minus_now])%mod

elif answer_type == 2:
    answer = 0
elif answer_type == 3:
    minuss = sorted(minuss, reverse = True)
    pluss = sorted(pluss)
    plus_now = 0
    minus_now = 0
    answer = 1
    for i in range(K):
        if plus_now < len(pluss):
            plus_target = pluss[plus_now]
        else:
            plus_target = 10000000000000
        
        if minus_now < len(minuss):
            minus_target = -minuss[minus_now]
        else:
            minus_target = 10000000000000  
        
        if plus_target <= minus_target:
            answer = (answer*plus_target)%mod
            plus_now += 1
        else:
            answer = (answer*minus_target)%mod
            minus_now += 1
    answer = answer * -1
print(answer%mod)