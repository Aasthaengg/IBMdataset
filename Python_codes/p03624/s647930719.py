S = input().strip()
for s in "abcdefghijklmnopqrstuvwxyz":
    if not s in S:
        print(s)
        exit()
print("None")
