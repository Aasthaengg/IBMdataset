N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(reverse=True, key=lambda x:x[0]+x[1])

t = sum(x[0] for x in AB[0::2])
a = sum(x[1] for x in AB[1::2])

print(t-a)
