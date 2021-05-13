n = int(input())
t = [0] + list(map(int, input().split()))

summ = sum(t)

for _ in range(int(input())):
    p, x = map(int, input().split())
    print(summ + x-t[p])