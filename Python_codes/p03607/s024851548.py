n = int(input())
a = [int(input()) for _ in range(n)]

a_set = set()
for a_i in a:
    a_set ^= {a_i}

print(len(a_set))
