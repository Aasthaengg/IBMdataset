str = input()
text = input()
ans = len(text)
for i in range(len(str) - len(text) + 1):
    dif = 0
    for j in range(len(text)):
        if not str[i+j] == text[j]:
            dif += 1
    ans = min(ans, dif)
print(ans)
