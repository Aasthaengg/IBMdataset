import sys
input=sys.stdin.readline

alp=[chr(i) for i in range(97, 97+26)]
s=input().rstrip()

for i in alp:
    if not i in s:
        print(i)
        exit()
print(None)