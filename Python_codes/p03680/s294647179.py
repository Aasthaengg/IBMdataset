n = int(input())
a = [int(input()) for _ in range(n)]
# a = list(map(lambda x: int(x) - 1, a))	#すべての要素から-1

p = a[0]

if p == 2:
    print(1)
    exit()
    
cnt = 1

for _ in range(n):
    p = a[p-1]
    cnt += 1
    if p == 2:
        print(cnt)
        exit()

print(-1)