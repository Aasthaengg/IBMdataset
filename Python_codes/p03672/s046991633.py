S = input()
m = len(S)//2

for i in range(len(S)):
    m -= 1
    if S[:m] == S[m:m*2]:
        print(m*2)
        break

