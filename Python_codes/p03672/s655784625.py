S = input()

n = len(S)
m = n // 2 if n % 2 == 1 else n//2 - 1

for w in range(m,0,-1):
    for i in range(w):
        if S[i] != S[i+w]:
            break
    else:
        print(2*w)
        break