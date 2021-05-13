n = int(input())
words = input()

count = 0
for i in range(n - 2):
  if words[i] == 'A':
    if words[i + 1] == 'B':
      if words[i + 2] == 'C':
        count += 1
print(count)
