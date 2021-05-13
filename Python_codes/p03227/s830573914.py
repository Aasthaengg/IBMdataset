s=list(input())
if len(s) == 2:
    print(*s, sep='')
else:
    print(*(s[::-1]), sep='')