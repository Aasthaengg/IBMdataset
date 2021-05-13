_ = input()
k = int(input())
x = [int(x) for x in input().split()]

ans = 0
for i in x:
    ans += min(i, k - i)
else:
    print(ans * 2)