s = input()
count = 0
for i in range (len(list(s))//2):
  if s[i] != s[-1-i]:
    count = count +1


print(count)