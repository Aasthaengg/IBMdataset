N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

ans = 0
minus = 0
plus_list = []
for a, b in zip(A, B):
    if a < b:
        ans += 1
        minus += b - a
    plus_list.append(a - b)

if minus == 0:
    print(0)
    exit()

plus_list_ = sorted(plus_list, reverse=True)

for p in plus_list_:
    minus -= p
    ans += 1
    if minus < 0:
        break

print(ans)
#print(minus)
#print(plus_list)