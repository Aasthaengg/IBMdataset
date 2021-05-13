s = input()

NUM_OF_ALPHABETS = 26

usable = [True for x in range(NUM_OF_ALPHABETS)]

for c in s:
    usable[ord(c) - ord('a')] = False

for i in range(NUM_OF_ALPHABETS):
    if usable[i]:
        print(s + chr(ord('a') + i))
        exit()

for i in range(len(s))[::-1]:
    index = ord(s[i]) - ord('a')
    usable[index] = True
    for j in range(index+1, NUM_OF_ALPHABETS):
        if usable[j]:
            print(s[0:i] + chr(ord('a') + j))
            exit()
print(-1)
