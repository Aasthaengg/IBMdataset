n = int(input())
blue_words = [input() for i in range(n)]
m = int(input())
red_words = [input() for i in range(m)]

ans = 0
for w in set(blue_words):
  tmp = blue_words.count(w) - red_words.count(w)
  if tmp > ans:
    ans = tmp

print(ans)