S = input()

alphabets = set(S)

ans = 100
for s in alphabets:
    ans = min(ans, max(list(map(len, S.split(s)))))

print(ans)