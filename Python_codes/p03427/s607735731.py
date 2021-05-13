N = input()

c = N[0]
ans = int(c) + 9 * (len(N) - 1)
if int(N) < int(c + '9' * (len(N) - 1)):
    ans -= 1
print(ans)