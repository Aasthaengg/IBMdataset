n =int(input())
min = n//1.08
max = n//1.08+1
ans = 0
if int(min*1.08) == n:
    ans = min
if int(max*1.08) == n:
    ans = max
if ans != 0:
    print(int(ans))
else:
    print(":(")
