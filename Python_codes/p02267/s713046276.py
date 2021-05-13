n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

print(sum(1 for i in t if i in s))

