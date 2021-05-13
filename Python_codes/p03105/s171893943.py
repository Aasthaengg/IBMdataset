s = list(map(int, input().split()))

if s[1]//s[0] > s[2]:
    print(s[2])
else:
    print(s[1]//s[0])
