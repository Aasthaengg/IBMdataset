from collections import Counter
N = int(input())
eaten = N - len(Counter(map(int, input().split())))
eaten += eaten & 1
print(N - eaten)
