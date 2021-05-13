N, K = map(int, input().split())
x = list(map(int, input().split()))
left = []
right = []
cnt = 0
for i in range(N):
    if x[i] < 0:
        left += [-x[i]]
    elif x[i] > 0:
        right += [x[i]]
    else:
        cnt += 1
rest = K - cnt
left = left[::-1]
if rest != 0:
    ans = float('inf')
else:
    ans = 0
    print(ans)
    exit()

for i in range(rest+1):
    if i == 0 and len(right) >= rest:
        ans = min(ans, right[rest-1])
    elif rest-i == 0 and len(left) >= i:
        ans = min(ans, left[rest-1])
    elif len(left) >= i and len(right) >= rest-i:
        ans = min(ans, left[i-1]+right[rest-i-1]+min(left[i-1], right[rest-i-1]))

print(ans)