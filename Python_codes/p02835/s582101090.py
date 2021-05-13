from collections import Counter, defaultdict
# n = int(input())
# li = list(map(int, input().split()))
# n = int(input())
a, b, c = map(int, input().split())
# d = defaultdict(lambda: 0)

# s = input()
print("win" if a+b+c<22 else "bust")