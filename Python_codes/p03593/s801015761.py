# 要求されるカルテットを条件ごとに求めて、その後要求されるペアを求めているが２つWA

from collections import Counter
w = ''
H,W = map(int,input().split())
for _ in range(H):
    w += input()
freq = Counter(list(w))
#print(freq)

quartet = 0
pair = 0
if H%2 == 0 and W%2 == 0:
    for v in freq.values():
        if v%4 != 0:
            print('No')
            exit()
    print('Yes')
    exit()

elif H%2 == 0 and W%2 != 0:

    for k,v in freq.items():
        #if freq[k] %4 ==0:
        if freq[k]>=4:
            quartet += v//4
            freq[k] -= 4*(v//4)
    if quartet < (H//2)*(W//2): # change slash //
        print('No')
        exit()
    else:
        pair += 2*(quartet-(H//2)*(W//2)) # 余分なカルテットをペアに分解

    for k,v in freq.items():
        if freq[k] >= 2:
            pair += v//2
            freq[k] -= 2*(v//2)
    if pair != H//2:
        print('No')
        exit()
    else:
        print('Yes')
        exit()


elif H%2 != 0 and W%2 == 0:
    for k, v in freq.items():
        #if freq[k] % 4 == 0:
        if freq[k] >= 4:
            quartet += v // 4
            freq[k] -= 4 * (v // 4)
    if quartet < (H // 2) * (W // 2):
        print('No')
        exit()
    else:
        pair += 2 * (quartet - (H // 2) * (W // 2))  # 余分なカルテットをペアに分解

    for k, v in freq.items():
        if freq[k] >= 2:
            pair += v // 2
            freq[k] -= 2 * (v // 2)
    if pair != W // 2:
        print('No')
        exit()
    else:
        print('Yes')
        exit()

else:
    for k, v in freq.items():
        if freq[k] >= 4:
            quartet += v // 4
            freq[k] -= 4 * (v // 4)
    if quartet < (H // 2) * (W // 2):
        print('No')
        exit()
    else:
        pair += 2 * (quartet - (H // 2) * (W // 2))  # 余分なカルテットをペアに分解

    for k, v in freq.items():
        #if freq[k] % 2 == 0:
        if freq[k] >=2:
            pair += v // 2
            freq[k] -= 2 * (v // 2)
    if pair != (W//2 + H//2):
        print('No')
        exit()
    else:
        print('Yes')
        exit()
