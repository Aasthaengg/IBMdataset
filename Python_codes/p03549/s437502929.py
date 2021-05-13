n,m = map(int,input().split())

# 全ての問題に正解する確率
all_ac = (0.5)**m

print(int((1900*m+100*(n-m))/all_ac))