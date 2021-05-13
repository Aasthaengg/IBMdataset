n = int(input())
a = list(map(int, input().split()))
cnt_a = [0] * (n + 1)
for ai in a:
    cnt_a[ai] += 1
print(*cnt_a[1:], sep='\n')