n = int(input())
s = list(input())

t = []

for c in s:
    if ord(c) + n > ord("Z") :
        t.append(chr(ord("A") + (ord(c) + n - ord("Z") - 1)))
    else:
        t.append(chr(ord(c) + n))

print("".join(t))