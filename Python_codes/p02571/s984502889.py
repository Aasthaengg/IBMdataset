S = input() # 本体
T = input() # 部分文字列

min_hamming = len(T)
for i in range(len(S) - len(T) + 1) :
    # print(S[i:i+len(T)], T, end = " ")
    hamming = 0
    for ch1, ch2 in zip(S[i:i+len(T)], T):
        hamming += 1 if ch1 != ch2 else 0
    # print(hamming)
    min_hamming = min(min_hamming, hamming)

print(min_hamming)