import sys
import string

sentence = sys.stdin.read().lower()
for c in string.ascii_lowercase:
    print('{} : {}'.format(c, sentence.count(c)))