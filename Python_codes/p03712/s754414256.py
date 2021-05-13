h, w = map(int, input().split())

s = '#' * (w+2)

print(s)

for _ in range(h):
    a = input()
    a = '#' + a + '#'
    print(a)

print(s) 