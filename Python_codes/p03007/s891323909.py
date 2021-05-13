N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

leftest_val = A[0]
rightest_val = A[-1]
left_idx = 1
right_idx = N - 2
history = []
for i in range(N - 1):
    left_val = A[left_idx]
    right_val = A[right_idx]
    if i == N - 2:
        history.append("{} {}".format(rightest_val, leftest_val))
        print(rightest_val - leftest_val)
    elif left_val < 0:
        history.append("{} {}".format(rightest_val, left_val))
        rightest_val -= left_val
        left_idx += 1
    else:
        history.append("{} {}".format(leftest_val, right_val))
        leftest_val -= right_val
        right_idx -= 1

for h in history:
    print(h)