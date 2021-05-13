import itertools

n = int(input())

a = list(input().split())
b = list(input().split())
str_a = ''.join(a)
str_b = ''.join(b)
li = [x for x in range(1, n+1)]
map = map(str, li)

p = itertools.permutations(map)
sorted_list = []
for v in p:
    tmp = ''.join(v)
    sorted_list.append(tmp)
sorted_list.sort()

ai = 0
bi = 0
for v in range(len(sorted_list)):
    if str_a == sorted_list[v]:
        ai = v
    elif str_b == sorted_list[v]:
        bi = v
res = abs(ai-bi)
if a == b: res = 0
print(res)