s = input()
gmp = 0

ans = 0
k = ''
for si in s:
    if si == 'g':
        if gmp > 0:
            ans += 1
            gmp -= 1
            k+='p'
        else:
            gmp += 1
            k+='g'
    else:
        if gmp > 0:
            gmp -= 1
            k+='p'
        else:
            gmp += 1
            ans -= 1
            k+='g'
# print(k)
print(ans)
