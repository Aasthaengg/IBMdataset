import sys

def main(s):
    counter=0
    cf=s[0]
    for x in s:
        if cf!=x:
            cf=x
            counter+=1
    return counter

s=sys.stdin.readline().strip()
print(main(s))
