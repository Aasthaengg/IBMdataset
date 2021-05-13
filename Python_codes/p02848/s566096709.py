alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
s = input()
ans = []
for i in range(len(s)):
    for j in range(len(alpha)):
        if s[i] == alpha[j]:
            if j+n<25:
                ans.append(alpha[j+n%26])
            else:
                ans.append(alpha[n%26-(26-j)])
print("".join(ans))