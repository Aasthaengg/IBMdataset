word = []
for i in range(2):
    word.append(raw_input())

num = word[0] + word[0]

if word[1] in num:
    print "Yes"
else:
    print "No"