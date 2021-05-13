S = input()

appeared = [False] * 26
for c in S:
    appeared[ord(c) - ord('a')] = True

for i in range(26):
    if not appeared[i]:
        print(chr(ord('a') + i))
        exit(0)

print("None")
