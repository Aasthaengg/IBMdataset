h,w = map(int,input().split())

lst = []
for _ in range(h):
    column = list(input())
    lst.append(column)
    lst.append(column)

for v in lst:
    print(''.join(v))