n = int(input())
temp_set = set()
for _ in range(n):
    a = input()
    if a in temp_set:
        temp_set.discard(a)
    else:
        temp_set.add(a)
print(len(temp_set))