from bisect import bisect_right
s = input()
t = input()

char_dic = dict()
for i in range(len(s)):
    if not s[i] in char_dic:
        char_dic[s[i]] = []
    char_dic[s[i]].append(i)

m = len(s)
i = 0
last_idx = -1
counter = dict()
for c in t:
    if not c in char_dic:
        print(-1)
        quit()
    j = bisect_right(char_dic[c], last_idx)
    if j == len(char_dic[c]):
        i += 1
        last_idx = char_dic[c][0]
    else:
        last_idx = char_dic[c][j]
print(i * len(s) + last_idx + 1)