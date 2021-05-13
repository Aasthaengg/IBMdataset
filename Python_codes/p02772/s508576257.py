n = int(input())
a = list(map(int, input().split()))
res = 'APPROVED'
for x in a:
    if x % 2 == 0 and x % 3 != 0 and x % 5 != 0:
        res = 'DENIED'
print(res)