h, w, a, b = map(int, input().split())

for i in range(b):
    ans = '0'*a + '1'*(w-a)
    print(ans)
for i in range(h-b):
    ans = '1'*a + '0'*(w-a)
    print(ans)