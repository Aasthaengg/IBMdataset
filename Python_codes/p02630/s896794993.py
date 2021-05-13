n = int(input())
a = list(map(int, input().split()))

a_dict = {}

for i in a:
    if not i in a_dict:
        a_dict[i] = 0
    a_dict[i] += 1

q = int(input())

s = sum(a)


for i in range(q):
    b, c = map(int, input().split())
    if not c in a_dict:
        a_dict[c] = 0
    s -= c * a_dict[c]

    if b in a_dict:
        s -= b * a_dict[b]
        a_dict[c] += a_dict[b]
    s += c * a_dict[c]

    a_dict[b] = 0

    print(s)