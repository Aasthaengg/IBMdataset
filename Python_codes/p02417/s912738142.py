import sys
sentence = ''
data = 'abcdefghijklmnopqrstuvwxyz'
for line in sys.stdin:
    sentence += line.lower()
for i in data:
    print(i + ' : ' + str(sentence.count(i)))