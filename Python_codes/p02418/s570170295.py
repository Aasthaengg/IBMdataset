s = input()
p = input()

s_long = s + s

judge = p in s_long
if judge:
    print('Yes')
else:
    print('No')

