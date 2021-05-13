h, w, a, b = map(int,input().split())

list_s = [0 for i in range(a)]
list_t = [1 for i in range(a)]

while len(list_s) != w:
    list_s.append(1)
    list_t.append(0)

s = ''.join(map(str, list_s))
t = ''.join(map(str, list_t))

for i in range(h):
    if i < b:
        print(s)
    else:
        print(t)
