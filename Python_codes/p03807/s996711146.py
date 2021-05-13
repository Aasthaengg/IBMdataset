n = int(input())
a = list(map(int,input().split()))

ki = sum(1 for i in a if i%2 == 1)

if ki%2 == 1:
    print("NO")
else:
    print("YES")