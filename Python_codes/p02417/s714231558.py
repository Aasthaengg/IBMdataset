import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"

string = sys.stdin.read()

for s in alphabet:
    print(s+" : "+str(string.lower().count(s)))
