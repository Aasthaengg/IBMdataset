h, w = map(int, input().split())
word1 = '#'*(w+2)
ans = list()
ans.append(word1)
for x in range(h):
    a = list(map(str, input().split()))
    word2 = '#' + "".join(a) + '#'
    ans.append(word2)

ans.append(word1)

for x in range(h+2):
    print(ans[x])
