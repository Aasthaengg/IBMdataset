s = input()
hmp = 0
ans = 0
for i in s:
    if i == 'g' and hmp > 0:
        hmp -= 1
        ans += 1
    elif i == 'g':
        hmp += 1
    elif hmp > 0:
        hmp -= 1
    else:
        hmp += 1
        ans -= 1
print(ans)