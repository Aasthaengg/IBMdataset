s = input()
i, j = 0, len(s)-1
while(1):
    if s[i] == "A":
        start = i
        break
    i += 1
while(1):
    if s[j] == "Z":
        end = j + 1
        break
    j -= 1
print(end - start)
