import sys

char = "abcdefghijklmnopqrstuvwxyz"
inp = sys.stdin.read()
for char_tmp in char:
    print(char_tmp + ' : ' + str(inp.lower().count(char_tmp)))