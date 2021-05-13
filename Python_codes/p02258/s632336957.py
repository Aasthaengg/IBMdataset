n=input()
min = input()
profit = None

for x in xrange(n-1):
    v = input()
    if profit is None:
        profit = v - min
    if profit < v - min:
        profit = v-min
    if min > v:
        min = v
print profit