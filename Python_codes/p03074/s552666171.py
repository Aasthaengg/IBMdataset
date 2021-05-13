N,K=map(int,input().split())
S=input()
seqs = [] #(start, end, 0or1): [start, end)
now_num = S[0]
start = 0
for i in range(1, N):
    if S[i] != now_num:
        seqs.append((start, i, int(now_num)))
        now_num = S[i]
        start = i
        if i == N-1:
            seqs.append((start, N, int(now_num)))
            break
    if i == N-1:
        seqs.append((start, N, int(now_num)))
        break

first = S[0]
zero_ranges = None
if first == "0":
    zero_ranges = [i for i in range(0, len(seqs), 2)]
else:
    zero_ranges = [i for i in range(1, len(seqs), 2)]
n_zero = len(zero_ranges)
if n_zero <= K:
    print(N)
    exit()

cum = [0]*(len(seqs)+1)
cum[0] = 0
for i in range(1, len(seqs)+1):
    s, e, n = seqs[i-1]
    cum[i] = cum[i-1] + e-s
length = len(seqs)
ans = 0
for i in range(int(first), len(seqs), 2):
    j = i + 2*K - 2
    if j+1 > length:
        continue
    tmp = 0
    if j+2 <= length and i-1 >= 0:
        tmp = cum[j+2] - cum[i-1]
    elif j+2 <= length and i-1 < 0:
        tmp = cum[j+2]
    elif j+2 > length and i-1 >= 0:
        tmp = cum[j+1] - cum[i-1]
    else:
        tmp = cum[j+1]
    ans = max(ans, tmp)
print(ans)