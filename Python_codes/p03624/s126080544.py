S=list(set(input()))
S.sort()
import string
switch=True
A=list(string.ascii_lowercase)
for i in A:
    if not i in S:
        print(i)
        switch=False
        break
if switch:
    print("None")