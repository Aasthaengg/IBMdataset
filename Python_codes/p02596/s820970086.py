import sys
k = int(input())

def a(n):
    t = n * 10 + 7
    return t % k

a_i = 7
i = 1
if a_i % k == 0:
    print(i)
    sys.exit()

for j in range(k+1):
    a_i = a(a_i)
    i += 1
    if a_i % k == 0:
        print(i)
        sys.exit()
print(-1)
