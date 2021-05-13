import re

a = str(input())

ans = re.match("[A-Z]",a)

if ans:
    print("A")
else:
    print("a")