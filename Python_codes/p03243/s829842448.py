N = int(input())
i = N // 111
if N%111 != 0:
    i += 1
print(i*111)