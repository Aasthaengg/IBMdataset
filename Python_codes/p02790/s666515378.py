a,b = map(str, input().split())
print(a*int(b) if ord(a) < ord(b) else b*int(a))