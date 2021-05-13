a, b, k = (int(i) for i in input().split())
s = set()
for i in range(a, a+k):
    if i >= a and i <= b:
        s.add(i)
for i in range(b-k+1, b+1):
    if i > a and i <= b:
        s.add(i)
s = sorted(list(s))
for a in s:
    print(a)