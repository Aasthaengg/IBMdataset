d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _i in range(d)]

last_days = [-1 for _i in range(26)]
result = []
for today in range(d):
    checker = [s[today][j]-c[j]*(today-last_days[j]) for j in range(26)]
    x = checker.index(min(checker))
    last_days[x] = today
    result.append(x+1)
for i in result:
    print(i)