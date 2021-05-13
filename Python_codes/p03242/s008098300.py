n = int(input())
for i in reversed(range(3)):
    if str(n)[-1*i - 1] == '1':
        n += 8*10**i
    elif str(n)[-1*i - 1] == '9':
        n -= 8*10**i
print(n)