change_K = int(input().split(" ")[-1])
word_S = list(input())
S = list(word_S)
word1 = ""
for i in range(change_K - 1):
    word1 = word1 + S[i]
word2 = S[change_K - 1]
word3 = ""
count = 0
while True:
    try:
        word3 = word3 + S[change_K + count]
        count += 1
    except IndexError:
        break
word2 = word2.swapcase()
print(word1 + word2 + word3)
