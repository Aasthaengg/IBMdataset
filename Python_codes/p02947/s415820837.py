n = int(input())

strings = {}

for i in range(n):
    s = "".join(sorted(list(input())))
    if s in strings:
        strings[s] += 1
    else:
        strings[s] = 1

print(sum(list(map(lambda x: x*(x-1)//2, strings.values()))))