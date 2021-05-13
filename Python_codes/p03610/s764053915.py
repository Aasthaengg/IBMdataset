input = str(input())

word = [x for x in input]
word = word[::2]

output = ""
for i in word:
  output += i
  
print(output)