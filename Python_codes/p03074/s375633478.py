def resolve():
    N, K = list(map(int, input().split()))
    S = input()
    seq = []
    cnt = 0
    for i in range(len(S)):
        if i == N-1 or S[i] != S[i+1]:
            seq.append([cnt+1, S[i]])
            cnt = 0
        else:
            cnt += 1
    #print(seq)
    left = 0
    right = 0
    maxlen = 0
    val = 0
    n_rev = 0
    for left in range(0, len(seq)):
        while (right < len(seq) and (n_rev < K or seq[right][1]=="1")):
            #print("left={}, right={}, n_rev={}".format(left, right, n_rev))
            cnt, state = seq[right]
            val += cnt
            if state == "0":
                n_rev += 1
            right += 1
        maxlen = max(maxlen, val)
        cnt, state = seq[left]
        val -= cnt
        if state == "0":
            n_rev -= 1
        if left == right:
            right += 1
    print(maxlen)
    

if '__main__' == __name__:
    resolve()