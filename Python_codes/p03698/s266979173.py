s = input()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
aa = [0]*26
ans = "yes"
for i in range(len(s)):
    for j in range(26):
        if s[i] == alphabet[j]:
            aa[j] += 1
            if aa[j] >= 2:
                ans = "no"
                break
print(ans)
