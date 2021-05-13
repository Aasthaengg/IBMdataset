import sys

N = int(sys.stdin.readline())
As = [int(x) for x in sys.stdin.readline().split(" ")]
Bs = [int(x) for x in sys.stdin.readline().split(" ")]

result = 0
for i in range(0, N):
    i = (N - 1) - i
    B = Bs[i]

    right = As[i + 1]
    right_result = min(B, right)
    result += right_result
    As[i + 1] -= right_result
    B -= right_result

    left = As[i]
    left_result = min(B, left)
    result += left_result
    As[i] -= left_result
    B -= left_result

print(result)
