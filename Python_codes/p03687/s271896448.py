S = str(input())
ans = 10 ** 9 + 7
for i in range(ord('a'), ord('z')+1):
    ans = min(ans, max([len(s) for s in S.split(chr(i))]))

print(ans)