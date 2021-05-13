n,x = map(int, input().split())
list = [int(input()) for _ in range(n)]
amari = x - sum(list)
print(amari//min(list)+len(list))