n = int(input())
S = list(map(int, input().split()))

q = int(input())
T = list(map(int, input().split()))

print(len([t for t in T if t in S]))
