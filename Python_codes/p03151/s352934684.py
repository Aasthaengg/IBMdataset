N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

plus = []
minus = []
for i in range(N):
    tmp = A[i] - B[i]
    if tmp > 0:
        plus.append(tmp)
    elif tmp < 0:
        minus.append(tmp)
        
plus = sorted(plus, reverse=True)

plus_cum = []
for i in range(len(plus)):
    if i == 0:
        plus_cum.append(plus[0])
    else:
        plus_cum.append(plus_cum[i-1] + plus[i])
        
minus_sum = sum(minus)
ans = -1
for i in range(len(plus_cum)):
    if plus_cum[i] >= -minus_sum:
        ans = i+1
        break

if len(minus) == 0:
    print(0)
elif ans == -1:
    print(ans)
else:
    print(ans + len(minus))