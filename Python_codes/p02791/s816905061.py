N = int(input())
P = list(map(int, input().split()))
f = False
count = 0
m = P[0]
for i in range(N):
    m = min(m, P[i])
    if m >= P[i]:
        count += 1


print(count)

    # print(i)
#     for j in reversed(range(0,i)):
#         # print(j)
#         if P[i] > P[j]:
#             f = True
        
#     if f == False:
#         count += 1
#     f = False
# print(count)
