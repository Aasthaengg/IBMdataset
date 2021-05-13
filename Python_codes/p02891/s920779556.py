S = input()
K = int(input())
cot = 0
before = ""
seq = []


for i in range(len(S)):
    c = S[i]
    if cot == 0:
        cot += 1
        before =c
    else:
        if c == before:
            cot += 1
        else:
            before = c
            seq.append(cot)
            cot = 1

seq.append(cot)
ans = 0
for temp in seq: #素の状態で連続してる文字列
    ans +=temp//2
ans *= K
if S[0] == S[-1]: #頭と尾で一緒→つなげたときに長い連続区間が発生
    ans += (seq[0] + seq[-1]) //2 * (K - 1) - (seq[0] //2 + seq[-1]//2 )* (K - 1)
if len(seq) == 1:
    ans = min(ans,seq[0] * K //2)
print(ans)