import sys
while True:
    n=0
    s=sys.stdin.readline()
    if s=='0\n': break
    for i in range(len(s)-1):
        n+=int(s[i])
    print(n)