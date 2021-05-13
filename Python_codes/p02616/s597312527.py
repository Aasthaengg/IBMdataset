N,K = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9+7

plus,minus,zero = 0,0,0
for i in range(N):
    if A[i] > 0:
        plus += 1
    elif A[i] < 0:
        minus += 1
    else:
        zero += 1

if N == K:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= MOD
    print(ans)

else:
    if K%2 == 1 and minus == N: # 負の場合
        A.sort(reverse=True)

        ans = 1
        for i in range(K):
            ans *= A[i]
            ans %= MOD
        print(ans)

    else: # そうじゃない場合
        l = []
        for i in range(N):
            if A[i] < 0:
                fugou = -1
            else:
                fugou = 1
            l.append((abs(A[i]),fugou))
        l.sort(reverse=True)
        #print(l)

        ans = 1
        fu = 0
        for i in range(K):
            if l[i][1] < 0:
                fu += 1
            ans *= l[i][0]
            ans %= MOD

        if fu%2 == 0:
            print(ans)
        elif ans == 0:
            print(0)
        else:
            sei_suteru = -1
            fu_suteru = -1
            for i in range(K)[::-1]:
                if sei_suteru == -1:
                    if l[i][1] > 0:
                        sei_suteru = l[i][0]
                if fu_suteru == -1:
                    if l[i][1] < 0:
                        fu_suteru = l[i][0]
                
            sei_ireru = -1
            fu_ireru = -1
            for i in range(K,N):
                if sei_ireru == -1:
                    if l[i][1] > 0:
                        sei_ireru = l[i][0]
                if fu_ireru == -1:
                    if l[i][1] < 0:
                        fu_ireru = l[i][0]

            #print(ans)
            #print(sei_suteru,fu_suteru,sei_ireru,fu_ireru)
            if sei_suteru >= 0 and fu_suteru >= 0 and sei_ireru >= 0 and fu_ireru >= 0:
                if sei_ireru*sei_suteru <= fu_ireru*fu_suteru: # 正を捨てて負を入れる方がいいとき
                    ans = -ans * -fu_ireru * pow(sei_suteru,MOD-2,MOD)
                    ans %= MOD
                else: # 負を捨てて正を入れる方がいいとき
                    ans = -ans * sei_ireru * pow(-fu_suteru,MOD-2,MOD)
                    ans %= MOD
            elif sei_ireru == -1 or fu_suteru == -1:
                ans = -ans * -fu_ireru * pow(sei_suteru,MOD-2,MOD)
                ans %= MOD
            else:
                ans = -ans * sei_ireru * pow(-fu_suteru,MOD-2,MOD)
                ans %= MOD

            print(ans)