n,l = map(int, input().split())

lst = []
for i in range(n):
    lst.append(l+i)
taste_total = sum(lst)
taste_pie = taste_total - min(lst, key = abs)

print(taste_pie)