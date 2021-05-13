N = int(input())
l = len(str(N))

if N <= 9:
    res = N
elif N%10**(l-1) == 10**(l-1)-1:
    res = N//10**(l-1) + 9*(l-1)
else:
    res = (N//10**(l-1) - 1) + 9*(l-1)
print(res)