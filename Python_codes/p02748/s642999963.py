A,B,M = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())

discount = []

for _ in range(M):
    x,y,c = map(int, input().split())
    discount.append([x-1,y-1,c])

ans_a = float('inf')
ans_b = float('inf')

for e in a:
    ans_a = min(ans_a, e)

for e in b:
    ans_b = min(ans_b, e)

ans = ans_a + ans_b

for x,y,c in discount:
    temp = a[x]+b[y]-c
    ans = min(ans, temp)

print(ans)