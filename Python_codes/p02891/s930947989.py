from copy import copy
def solve():
    S = input()
    K = int(input())
    ans = 0
    seqs = []
    seq = 1
    for i in range(1,len(S)):
        if S[i]==S[i-1]:
            seq += 1
        else:
            seqs.append(seq)
            seq = 1
    seqs.append(seq)
    first_seq = seqs[0]
    last_seq = seqs[-1]
    seqs.pop(0)
    if len(seqs):
        ans += first_seq//2 + last_seq//2
        seqs.pop(-1)
        if S[0]==S[-1]:
            ans += ((first_seq + last_seq)//2)*(K-1)
        else:
            ans *= K
        ans += sum(map(lambda x: x//2,seqs))*K
    else:
        if S[0]==S[-1]:
            ans += first_seq*K//2
        else:
            ans += first_seq//2*K
    return ans
print(solve())