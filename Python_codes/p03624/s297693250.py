import collections

s = input()
c = collections.Counter(s)

for i in range(26):
    alpha = chr(i + ord("a"))
    if c[alpha] == 0:
        print(alpha)
        break
else:
    print("None")
