s = input()

a = s[len(s) - 1]

#print(a)

if a == "s":
    s = s + "es"
else:
    s = s + "s"

print(s)