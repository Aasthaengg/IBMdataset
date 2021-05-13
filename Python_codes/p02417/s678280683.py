count = [0 for _ in range(ord("a"), ord("z") + 1)]
while True:
    try:
        for c in list(input().lower()):
            if "a" <= c <= "z":
                count[ord(c) - ord("a")] += 1
    except EOFError:
        break
for i, n in enumerate(count):
    print("{ch} : {cnt}".format(ch = chr(ord("a") + i), cnt = n))


