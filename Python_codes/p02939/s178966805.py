S = list(input())

i = 1
r = len(S)
while True:
    if i >= len(S):
        break
    if S[i-1] == S[i]:
        r -= 1
        i += 2
    i += 1

print(r)