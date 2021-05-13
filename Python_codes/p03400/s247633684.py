n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

ch = x
for ai in a:
    ch += (d - 1) // ai + 1
print(ch)
