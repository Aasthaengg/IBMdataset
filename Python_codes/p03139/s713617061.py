n,a,b = map(int, input().split())

min_num = min(a,b)
max_num = max(a+b-n,0)

print(min_num, max_num)