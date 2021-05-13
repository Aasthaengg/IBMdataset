s = input()
k = int(input())

for i in range(len(s)):
    if s[i] != "1" and i+1 <= k:
        print(s[i])
        exit()

print(1)