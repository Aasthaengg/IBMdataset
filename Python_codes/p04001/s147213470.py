from itertools import product

S = input()

patterns = list(product(["","+"],repeat=len(S)-1))

ans = 0

for pattern in patterns:
    cnt = 0
    num = ""
    for i in range(len(pattern)+1):
        if i == 0:
            num = num + S[i]
        else:
            if pattern[i-1] == "+":
                cnt += int(num)
                num = S[i]
            else:
                num = num + S[i]
    cnt += int(num)
    ans += cnt


print(ans)