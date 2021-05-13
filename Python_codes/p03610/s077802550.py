s = input()
word = ''
for i in range((len(s)+1)//2):
	word += s[2*i]
print(word)