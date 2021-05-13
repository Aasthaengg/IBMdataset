S = input()

if len(S) == 1:
    print(0)
    exit()

c0 = S[0]
cnt = 0
for c in S[1:]:
    if c != c0:
        c0 = c
        cnt += 1 
print(cnt)