n = int(input())
mx = 1
i = 1
while i**2 <= n:
    mx = i**2
    i += 1
print(mx)