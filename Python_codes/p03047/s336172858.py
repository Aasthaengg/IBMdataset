tmp = input()
nul = tmp.rfind(' ')
n = int(tmp[:nul:])
k = int(tmp[nul + 1::])

print(n - (k - 1))