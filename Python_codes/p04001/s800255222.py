

def susiki(n, s, dest):
    if n == len(s):
        tmp = 0
        pre = 0
        for d in dest:
            tmp += int(s[pre:d])
            pre = d
        tmp += int(s[pre:])
        return tmp
    return susiki(n+1, s, dest+[n]) + susiki(n+1, s, dest)

s = input()
l = len(s)

print(susiki(1, s, []))