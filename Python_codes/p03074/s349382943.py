# 累積和による解法
def resolve():
    N, K = list(map(int, input().split()))
    S = input()
    seq = []
    cnt = 0
    if S[0] != "1":
        seq.append(0)
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            seq.append(cnt+1)
            cnt = 0
        else:
            cnt += 1
    seq.append(cnt+1)
    if S[-1] != "1":
        seq.append(0)
    #print(seq)

    cum = [0]
    cur = 0
    for c in seq:
        cur += c
        cum.append(cur)
    #print(cum)
    
    maxlen = len(S) if len(cum) <= (2*K+1) else 0
    for i in range(0, len(cum)-(2*K+1), 2):
        l = cum[i+(2*K+1)] - cum[i]
        maxlen = max(maxlen, l)
    print(maxlen)
    

if '__main__' == __name__:
    resolve()