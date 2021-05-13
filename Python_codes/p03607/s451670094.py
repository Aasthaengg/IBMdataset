n = int(input())
a = [int(input()) for _ in range(n)]

my_set = set()

for item in a:
    if item in my_set:
        my_set.remove(item)
    else:
        my_set.add(item)

print(len(my_set))
