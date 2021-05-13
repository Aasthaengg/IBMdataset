s = input()
k = int(input())

for i in range(len(s)):
    if s[i] != '1':
        if k > i:
            print(int(s[i]))
        else:
            print(1)
        exit()

print(1)
