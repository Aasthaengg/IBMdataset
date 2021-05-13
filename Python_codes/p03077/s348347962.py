n = int(input())
ans = 0
lst = [int(input()) for _ in range(5)]
min_num = min(lst)
print((n+min_num-1)//min_num + 4)
