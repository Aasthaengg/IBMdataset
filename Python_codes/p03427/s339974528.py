N = input()
ans = 0

if N[1:] == "9" * (len(N) - 1):
    ans = int(N[0]) + (9 * (len(N) - 1))
else:
    ans = int(N[0]) + 9 * (len(N) - 1) - 1

print(ans)
