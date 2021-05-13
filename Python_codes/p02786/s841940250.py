H=int(input())

sum = 0
i = 0
while H > 0:
    i += 1
    hits = 2**(i-1)
    sum += hits
    if H == 1:
        H = 0
    else:
        H //= 2

print(sum)
