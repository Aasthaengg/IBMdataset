S = input()

ans = 1000
for i in range(len(S)-2):
    num = 100*int(S[i]) + 10*int(S[i+1]) + int(S[i+2])
    if ans > abs(753-num):
        ans = abs(753-num)

print(ans)