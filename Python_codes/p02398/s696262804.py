line = input()
words = line.split()
count = 0
for i in range(int(words[0]), int(words[1])+1):
    if (int(words[2]) % i == 0):
        count += 1
print(count)