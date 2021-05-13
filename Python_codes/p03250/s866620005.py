l = list(input().split())
l.sort(reverse=True)
print(int(''.join(l[:2])) + int(l[2]))