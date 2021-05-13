rp = input().split()
n = len(rp)-1
i = 1
while n:
    if rp[i] in ('+', '-', '*'):
        i -= 1
        rp[i], rp[i+1] = rp[i+1], rp[i]
        rp[i-1] = str(eval(''.join(rp[i-1:i+2])))
        del rp[i:i+2]
        n -= 2
    else:
        i += 1
print(*rp)