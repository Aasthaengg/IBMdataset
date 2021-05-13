n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = sum(B) - sum(A)
cnt_a, cnt_b = 0, 0

for a, b in zip(A, B):
    if a > b:
        cnt_b += 1
    elif a < b:
        if (b-a) % 2 == 0:
            cnt_a += (b-a)//2
        else:
            cnt_a += (b-a)//2 + 1

if max(cnt_a, cnt_b) <= m:
    print('Yes')
else:
    print('No')