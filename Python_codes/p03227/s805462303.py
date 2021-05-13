s = list(input())
if len(s) == 2:
    print(*s, sep="")
else:
    s.reverse()
    print(*s, sep="")