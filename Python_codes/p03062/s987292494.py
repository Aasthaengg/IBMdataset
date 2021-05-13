N = int(input())
A = list(map(int,input().split()))
Sum = 0
Min = float("inf")
cnt = 0
zero = 0

for i in A:
    Min = min(Min,abs(i))
    Sum  += abs(i)
    if i < 0:
        cnt += 1
    elif i == 0:
        zero += 1

if cnt % 2 == 0:
    print(Sum)
elif zero > 0:
    print(Sum)
else:
    print(Sum-2*Min)