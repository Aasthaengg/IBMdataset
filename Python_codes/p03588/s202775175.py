n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(max(s)[0] + max(s)[1])