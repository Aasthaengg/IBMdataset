a,b = map(int, input().split())
M = [int(input()) for _ in range(a)]
print(int((b-sum(M))//min(M)) + a)