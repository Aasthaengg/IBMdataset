a = input()
b = input()
if len(a)<len(b):
    print("LESS")
elif len(a)==len(b):
    print("LESS" if a<b else "EQUAL" if a==b else "GREATER")
else:
    print("GREATER")