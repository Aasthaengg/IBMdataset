n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = [0, 0]
for ea, eb in zip(a, b):
    if ea > eb:
        cnt[1] += ea - eb
    else:
        cnt[0] += (eb - ea) // 2

if cnt[0] >= cnt[1]:
    ans = "Yes"
else:
    ans = "No"
print(ans)
