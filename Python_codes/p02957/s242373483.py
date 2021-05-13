# from collections import Counter
# n = int(input())
# li = list(map(int, input().split()))
a, b = map(int, input().split())
print(a+(b-a)//2 if not (b-a)&1 else "IMPOSSIBLE")
