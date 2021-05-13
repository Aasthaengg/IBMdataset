n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
count = []
mx = 0
words_list = list(set(s+t))
for word in words_list :
    count.append([word, 0])
for word in words_list :
    idx = words_list.index(word)
    count[idx][1] += s.count(word)
    count[idx][1] -= t.count(word)
for i in range(len(words_list)) :
      mx = max(mx,count[i][1])
print(mx)
