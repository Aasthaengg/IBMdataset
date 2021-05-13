a = [[['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
[['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
 [['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
 [['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
n = input()
for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    a[b - 1][f - 1][r] += v
print ' '.join(map(str, a[0][0]))
print ' '.join(map(str, a[0][1]))
print ' '.join(map(str, a[0][2]))
print '####################'
print ' '.join(map(str, a[1][0]))
print ' '.join(map(str, a[1][1]))
print ' '.join(map(str, a[1][2]))
print '####################'
print ' '.join(map(str, a[2][0]))
print ' '.join(map(str, a[2][1]))
print ' '.join(map(str, a[2][2]))
print '####################'
print ' '.join(map(str, a[3][0]))
print ' '.join(map(str, a[3][1]))
print ' '.join(map(str, a[3][2]))