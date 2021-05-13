s = str(input())
k = int(input())
for i in range(len(s)):
    if s[i] != '1' or k - 1 == i:
        print(s[i])
        exit()