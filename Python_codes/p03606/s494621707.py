N = int(input())
i =0
ans =0

while i < N:
    a = input().split()
    ans += int(a[1]) - int(a[0]) +1
    i = i + 1
print(ans)