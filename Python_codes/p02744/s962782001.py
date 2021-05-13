#coding: utf-8

n = int(input())

def f(level):
    if level == 1:
        return ["a"]
    ret = []
    for x in f(level-1):
        s = sorted(list(set( (c for c in x))))
        s.append(chr(ord(s[-1])+1))
        for c in s:
            ret.append(x + c)
    return ret

print("\n".join(f(n)))

