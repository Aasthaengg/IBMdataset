N = int(input())
if set(list(str(N))) == {"9"}:
    print(9 * len(str(N)))
elif N < 10:
    print(N)
elif set(list(str(N)[1:])) == {"9"}:
    print(int(str(N)[0]) + 9 * len(str(N)[1:]))
else:
    print(9 * (len(str(N)) - 1) + int(str(N)[0]) - 1)
