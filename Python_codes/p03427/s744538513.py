N = int(input())

if N < 10:
    print(N)
    exit()

n = N - int((len(str(N)) - 1) * '9')
tmp = (len(str(N)) - 1) * '9'
if len(str(n)) > (len(str(N)) - 1):
    tmp = str(n)[0] + tmp

res = 0
for t in tmp:
    res += int(t)

print(res)
