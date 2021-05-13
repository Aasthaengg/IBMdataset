import sys
s=input()
alphabet=[chr(i) for i in range(97,97+26)]
for i in alphabet:
    if s.count(i)>=2:
        print("no")
        sys.exit()
print("yes")