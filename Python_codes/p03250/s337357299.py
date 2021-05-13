s = list(input().split())
s = sorted(s,reverse = True)
print(int(''.join(s[:2]))+int(s[2]))