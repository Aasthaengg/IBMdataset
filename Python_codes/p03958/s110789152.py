k,t = map(int, input().split())
a = sorted(list(map(int, input().split())))
Sum = sum(a)-a[-1]
Max = a[-1]
if Sum >= Max: ans = 0
else: ans = Max-Sum-1
print(ans)