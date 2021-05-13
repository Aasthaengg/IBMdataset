import re
n=int(input())
s=input()
result = re.findall(r'ABC', s)
print(len(result))