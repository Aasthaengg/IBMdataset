s = input()

ans = 0
if s == 'RRR':
    ans = 3
elif s == 'RRS' or s == 'SRR':
    ans = 2
elif s == 'SSS':
    ans = 0
else:
    ans = 1

print(ans)