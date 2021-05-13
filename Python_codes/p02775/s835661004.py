N = input()
DP = [0,0]
kuriagari = 0
kuriagarazu = 0
for n in N:
    n = int(n)
    kuriagaru = 11 - n + kuriagari
    kuriagaranai = n + kuriagarazu
    DP.append([kuriagaru, kuriagaranai])
    kuriagari = DP[-1][0] - 2 if DP[-1][0] - 2 < DP[-1][1] else DP[-1][1]
    kuriagarazu = DP[-1][0] if DP[-1][0] < DP[-1][1] else DP[-1][1]

answer = min(DP[-1])
print(answer)