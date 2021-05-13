n, k = map(int, input().split())
s = input()

s = '1' + s + '1'

cnt_1 = []
cnt_0 = []
stack_1 = 0
stack_0 = 0
for i in s:
    if i == '1':
        if stack_0 > 0:
            cnt_0.append(stack_0)
            stack_0 = 0
        stack_1 += 1
    else:
        if stack_1 > 0:
            cnt_1.append(stack_1)
            stack_1 = 0
        stack_0 += 1
if stack_1 > 0:
    cnt_1.append(stack_1)

if len(cnt_1) == 0 or len(cnt_0) == 0:
    print(n)
    exit()
cnt_1[0] -= 1
cnt_1[-1] -= 1

if k > len(cnt_0):
    k = len(cnt_0)
cum_1 = [sum(cnt_1[:k+1])]
cum_0 = [sum(cnt_0[:k])]
for i in range(1, len(cnt_1)-k):
    cum = cum_1[i-1] + cnt_1[i+k] - cnt_1[i-1]
    cum_1.append(cum)
for i in range(1, len(cnt_0)-k+1):
    cum = cum_0[i-1] + cnt_0[i+k-1] - cnt_0[i-1]
    cum_0.append(cum)
res = []

for v, w in zip(cum_1, cum_0):
    res.append(v+w)
print(max(res))