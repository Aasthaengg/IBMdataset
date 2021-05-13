N = int(input())
m = {
    'S': list(range(1, 14)),
    'H': list(range(1, 14)),
    'C': list(range(1, 14)),
    'D': list(range(1, 14))
}
for i in range(N):
    shape, num = input().strip().split(' ')
    num = int(num)
    m[shape].remove(num)
for k in ['S', 'H', 'C', 'D']:
    if len(m[k]) > 0:
        for x in m[k]:
            print('%s %d' % (k, x))