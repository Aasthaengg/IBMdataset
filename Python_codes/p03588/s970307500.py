N = int(input())

AB = [list(map(int,input().split())) for _ in range(N)]

AB.sort(reverse=True)

print(sum(AB[0]))