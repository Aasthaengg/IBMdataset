N = int(input())
S = [input() for _ in range(N)]

word_list = {}

for i in range(N):
    if S[i] in word_list:
        word_list[S[i]] += 1
    else:
        word_list[S[i]] = 1

word_list_s = sorted(word_list.items(), key=lambda x:x[1], reverse=True)
word_list_s_max = []
for i in range(len(word_list_s)):
    if word_list_s[i][1] == word_list_s[0][1]:
        word_list_s_max.append(word_list_s[i])
word_list_s_2 = sorted(word_list_s_max, key=lambda x:x[0])

for i in range(len(word_list_s_2)):
    print(word_list_s_2[i][0])