N = int(input())

if N == 0:
    print(0)
    exit()
elif N == 1:
    print(1)
    exit()
DP = [(0,1)]
num = 0
start = 0
end = 1
while True:
    num += 1
    a = end - start + 1
    if num % 2 == 0:
        start_ = end + 1
        end_ = start_ + a - 1
        end = end_
    else:
        end_ = start - 1
        start_ = end_ - a + 1
        start = start_
    DP.append((start_, end_))
    if start <= N <= end:
        break

Ans = ''
DP[0] = (1, 1)
for i, (start, end) in enumerate(DP[::-1]):
    if start <= N <= end:
        Ans += '1'
        N -= (-2) ** (num-i)
    else:
        Ans += '0'

print(Ans)
