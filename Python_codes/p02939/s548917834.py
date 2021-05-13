# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    s = input().rstrip()

    g = []
    if s[0] != s[1]:
        g.append(1)
        g.append(2)
        if s[1] == s[2]:
            g.append(2)
        else:
            g.append(3)
    else:
        g.append(1)
        g.append(1)
        g.append(2)


    for i in range(3, len(s)):
        if s[i] == s[i-1]:
            g.append(g[i-3]+2)
        else:
            g.append(g[i-1]+1)

    print(g[len(g)-1])




if __name__ == "__main__":
    resolve()
