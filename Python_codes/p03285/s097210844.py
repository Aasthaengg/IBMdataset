N = int(input())

p_list = []
for a in range(26):
    for b in range(16):
        p = 4 * a + 7 * b
        p_list.append(p)
a = p_list.count(N)
if a > 0:
    print('Yes')
else:
    print('No')