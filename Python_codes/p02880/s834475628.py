n = int(input())
s = {1}

for i in range(1, 10):
    for k in range(1, 10):
        s.add(i * k)

if n in s:
    print('Yes')
else:
    print('No')
