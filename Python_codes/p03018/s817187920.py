import sys
# input = sys.stdin.readline

def main():
    s = list(input().replace("BC", "D"))
    a = 1
    for i in range(len(s)-1):
        w = "".join(s[i:i+2])
        if w == "AD":
            s[i], s[i+1] = "D", "A"
            yield a
        elif w == "AA":
            a += 1
        else:
            a = 1


print(sum(main()))
