# from collections import Counter
# n = int(input())
# li = list(map(int, input().split()))
# a, b = map(int, input().split())
# a = int(input())
s = input()
r = input()
print(sum(1 if s[i] == r[i] else 0 for i in range(len(s))))
