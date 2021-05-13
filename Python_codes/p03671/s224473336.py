a, b, c = map(int, input().split())

list_a = []
list_a.append(a)
list_a.append(b)
list_a.append(c)


list_a.sort()

print(list_a[0] + list_a[1])