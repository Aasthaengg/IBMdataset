n = int(input())
a = list(map(int, input().split()))

b = [abs(i) for i in a]

if sum([i <= 0 for i in a]) % 2 == 0:
    print(sum(b))
else:
    print(sum(b) - min(b) * 2)