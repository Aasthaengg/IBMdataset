n = int(input())
s = str(input())
k = int(input())
word = ""
w = s[k-1]
for i in s:
    if w != i:
        word += "*"
    else:
        word += w
print(word)