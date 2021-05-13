s = input()
k = int(input())

for i in range(max(k, len(s))):
    if s[i] != '1' or i == k - 1:
        print(s[i])
        break
