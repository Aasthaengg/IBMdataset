word = input()

string = input().lower()
last = ""

while last != "END_OF_TEXT":
	last = input()
	string += " " + last.lower()

list_words = list(string.split())

count = 0

for s in list_words:
	if s == word:
		count += 1

print(count)