w = list(input())
s = list(set(w))
for i in s:
    if w.count(i)%2:
        print("No")
        exit()
print("Yes")