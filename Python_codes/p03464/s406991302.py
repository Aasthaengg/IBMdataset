K = int(raw_input())
A = map(int, raw_input().split())

ma = mi = 2
for a in reversed(A):
    mi = (mi + a - 1) // a * a
    ma = (ma ) // a * a + a - 1
if mi <= ma:
    print mi, ma
else:
    print -1