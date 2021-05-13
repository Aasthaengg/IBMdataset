word = str(input())
even = word[1::2]
odd = word[::2]
if ("R" in even) or ("L" in odd):
    print("No")
else:
    print("Yes")