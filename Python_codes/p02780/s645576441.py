N, K = map(int, input().split())
dice = list(map(int, input().split()))

#dice.sort(reverse=True)
MAXX = 1001
ave = [0.0]*MAXX

ans = 0.0
sumz = [0.0]*(N+1)
right = 0
#累積和
for i in range(N):
    x = dice[i]
    if ave[x] <= 0.000001:
        ave[x] = (x + 1) / 2.0
    sumz[i+1] = sumz[i]+ ave[x]

#find max
for i in range(K, N+1):
    if ans < sumz[i] - sumz[i-K]:
        ans = sumz[i] - sumz[i-K]

print(ans)
#
# for left in range(0, N):
#     if right <= left: right = left
#     while right < N and right - left <= K:
#         x = dice[right-1]
#         if ave[x] <= 0.000001:
#             ave[x] = (x+1)/2.0
#         sumz[right] = sumz[right-1] + ave[x]
#         right += 1
#
#     if ans < sumz[right-1]:
#         ans = sumz[right-1]
#
# print(ans)
#
#
#
#
#
# print(ans)
