N = int(input())
S = input()
idx = 0
res = 0
while idx + 2 < N:
    if S[idx] == 'A':
        if S[idx:idx+3] == 'ABC':
            res += 1 
            idx += 3
            continue
    idx += 1
print(res)