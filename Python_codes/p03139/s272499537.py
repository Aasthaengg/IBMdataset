n,a,b = map(int,input().split())
max_ans = min(a,b)
min_ans = max(0, (a + b) - n)
print(max_ans, min_ans)