s = input()

ans = True
while s != "":
    words = ["eraser", "dream", "erase", "dreamer"]

    found = False
    for word in words:
        if s[-len(word):] == word:
            s = s[:-len(word)]
            found = True
            break

    if not found:
        ans = False
        break

print("YES" if ans else "NO")