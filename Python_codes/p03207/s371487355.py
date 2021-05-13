s = int(input())
a = 0
ans = 0
for i in range(s):
    i = int(input())
    ans += i
    if a<i:
        a = i
ans -= a/2
print(int(ans))