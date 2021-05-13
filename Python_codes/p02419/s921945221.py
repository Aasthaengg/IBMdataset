w = input().lower()
t = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    for word in s.lower().split():
        t.append(word)
print(t.count(w))