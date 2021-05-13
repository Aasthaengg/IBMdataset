n = int(input())
s = set(map(int, input().split()))
q = int(input())
t = set(map(int, input().split()))

ans = s & t
print(len(ans))
