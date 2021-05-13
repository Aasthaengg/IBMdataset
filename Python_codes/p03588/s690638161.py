n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(reverse=True)
print(ab[0][0]+ab[0][1])