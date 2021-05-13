N = int(input())

ans = ''
if N == 0:
    print(0)
    exit()

while N != 0 and N != 1:
    if N > 0:
        if N%2:
            ans += '1'
            N = -(N//2)
        else:
            ans += '0'
            N = -N//2
    else:
        if -N%2:
            ans += '1'
            N = -(N-1)//2
        else:
            ans += '0'
            N = N//(-2)
if N:
    ans += '1'
print(ans[::-1])

