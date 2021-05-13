N = int(input())
A = list(map(int, input().split()))

cnt4 = 0
cnt2 = 0
for a in A:
    if a % 4 == 0:
        cnt4 += 1
    elif a % 2 == 0:
        cnt2 += 1

ans = "No"

if N - cnt4*2 <= 1:
    ans =  "Yes"
elif N - cnt4*2 > 1:
    if N - cnt4*2 <= cnt2:
        ans = "Yes"
elif N - cnt4*2 == N:
    if N == cnt2*2:
        ans = "Yes"

print(ans)