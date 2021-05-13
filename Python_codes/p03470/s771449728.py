n = int(input())

mochi_list = []
for i in range(n):
    mochi_list.append(input())

mochi_unique = list(set(mochi_list))

print(len(mochi_unique))