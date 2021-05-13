n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
c = 0

for i in a:
    c += (d-1)//i+1

print(c+x)
