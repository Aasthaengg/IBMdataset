n = str(input())
w = ""
for i in n:
    if i == "9":
        w += "1"
    else:
        w += "9"
print(w)