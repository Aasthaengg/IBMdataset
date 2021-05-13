N,K = map(int,input().split())
S = list(input())

c = 0  #初期状態の幸せな人数
d = 0  #左から見ていって何回向きが変わるか
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        c += 1
    else:
        d += 1

if d >= 2*K:
    print(c+2*K)
else:
    print(c+d)