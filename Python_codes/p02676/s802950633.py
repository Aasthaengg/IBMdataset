k = int(input())
s = list(input())

if len(s) <= k:
    print(''.join(s))
    exit()

s_sub = s[:k]
print(''.join(s_sub) + '...')
