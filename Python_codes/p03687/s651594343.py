S = input()
alphabets = [chr(ord('a') + x) for x in range(26)]

ans = 10000
for c in alphabets:
    ans = min(ans, max([len(f) for f in S.split(c)]))
print(ans)
