text = input()
w = input()

circle = text+text[:-1]

if circle.find(w) != -1:
    print("Yes")
else:
    print("No")
