N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

assign_plus = 0
minus = 0

for i in range(N):
    assign_plus += max(0, (b[i]-a[i])//2)
    minus += max(0, a[i]-b[i])

if assign_plus >= minus:
    print("Yes")
else:
    print("No")