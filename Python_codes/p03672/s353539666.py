import sys
s=list(input())
for i in range(len(s)//2):
    s=s[:-2]
    sa=s[:len(s)//2]
    sb=s[len(s)//2:]
    if sa==sb:
        print(len(s))
        sys.exit()