N = int(input())
a = list(map(int, input().split()))
MIN = min(a)
MAX = max(a)
answer = MAX - MIN
print(answer)