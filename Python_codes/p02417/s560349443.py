import string
import sys

input_str = sys.stdin.read()

for i in range(26):
    char = string.ascii_lowercase[i]
    CHAR = string.ascii_uppercase[i]
    cnt = input_str.count(char) + input_str.count(CHAR)
    print("{0} : {1}".format(char, cnt))