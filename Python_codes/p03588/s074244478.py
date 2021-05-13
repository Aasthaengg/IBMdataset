n = int(input())
AB = sorted([ list(map(int, input().split())) for _ in range(n) ])
print(sum(AB[::-1][0]))