# list関数を使う
# list関数のリスト内包表記
s, t = (list(a for a in input()) for b in range(0, 2))
count = 0
length = len(s)
for i in range(length):
    if s[i] != t[i]: count += 1

print(count)