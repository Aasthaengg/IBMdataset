N = int(input())
TA = []
for i in range(N):
    T, A = map(int, input().split())
    TA.append((T, A))

T, A = TA[0]
answer = T+A
p = 1
prev = p
pT, pA = T, A
for i in range(1,N):
    # (T+A) * p >= prev
    # p >= prev/(T+A)
    T, A = TA[i]
    s = T+A
    p = (answer+s-1)//s
    p1 = (pT+T-1)//T
    p2 = (pA+A-1)//A
    p = max([p,p1,p2])
    pT, pA = p*T, p*A
    answer =  pT+pA
    #print(T, A, p, answer, sep="\t")
print(answer)

    
