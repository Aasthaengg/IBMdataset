n = int(input())
list_d = []
for _ in range(n):
    a, b = map(int, input().split())
    list_d.append(a == b)
for i in range(n-2):
    if list_d[i] and list_d[i+1] and list_d[i+2]:
        print('Yes')
        exit()
print('No')