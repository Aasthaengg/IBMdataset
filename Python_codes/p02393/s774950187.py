a = map(int, raw_input().split())

a.sort()
a = map(str, a)

print a[0] + ' ' + a[1] + ' ' + a[2]