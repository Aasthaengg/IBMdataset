N = int(input())
start = 0
end = 1
Judge = [(1, 1)]
for i in range(1, abs(N)):
    start_ = start + (-2) ** i
    end_ = end + (-2) ** i
    Judge.append((start_, end_))
    start = min(start, start_)
    end = max(end, end_)
    if start <= N <= end:
        break

n = len(Judge)
A = ['0'] * n

for i in range(n)[::-1]:
    start, end = Judge[i]
    if start <= N <= end:
        A[i] = '1'
        N -= (-2) ** i
print(''.join(A[::-1]))
