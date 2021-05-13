s = raw_input()
s = s.split(' ')
s = [int(x) for x in s]
n, m = s

print((n-1)*(m-1))