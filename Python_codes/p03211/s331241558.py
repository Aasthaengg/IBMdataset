s = input()
ans = 753*2

for i in range(len(s)-2):
    sanko = list(map(int,(s[i:i+3])))
    kazu = sanko[0]*100 + sanko[1]*10 + sanko[2]

    if abs(kazu-753) < ans:
        ans = abs(kazu-753)

print(ans)
