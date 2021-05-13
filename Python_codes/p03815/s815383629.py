n = int(raw_input())
h = {0:0}
for i in range(1, 6+1): h[i] = 1
for i in range(7, 12): h[i] = 2
print 2 * (n / 11) + h[n % 11]