w = input()
a = []
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    t = t.split()
    a.append(t)
ans = list(item.lower() for innerlist in a for item in innerlist)
print(ans.count(w))