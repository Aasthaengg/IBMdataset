S = input()
ans = -1
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in S:
        continue
    else:
        ans = S + chr(i)
        print(ans)
        exit()
R = set()
for i, s in enumerate(S[::-1], 1):
    for j in range(ord(s)+1, ord('z')+1):
        if chr(j) in R:
            ans = S[:-i] + chr(j)
            print(ans)
            exit()
    R.add(s)
print(ans)

