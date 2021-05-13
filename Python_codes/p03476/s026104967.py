q = int(input())
LR = [0]*q
for i in range(q):
    LR[i] = list(map(int,input().split()))
lis = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317]

p_lis = [0]*(1+10**5)
for i in range(3,10**5+1):
    sw1 = 1
    sw2 = 1
    for P in lis:
        if P > i**0.5:
            break
        if i%P == 0:
            sw1 = 0
            break
        
    if sw1 == 1:
        for P in lis:
            if P > ((i+1)//2)**0.5:
                break
            if (i+1)//2%P == 0:
                sw2 = 0
                break
            
    if sw1 == 1 and sw2 == 1:
        p_lis[i] = 1
s_lis = [0]*(1+10**5)
for i in range(1,len(p_lis)):
    if p_lis[i] == 1:
        s_lis[i] = s_lis[i-1] + 1
    else:
        s_lis[i] = s_lis[i-1]
for L,R in LR:
    print(s_lis[R]-s_lis[L-1])
