N = int(input())
A = [int(x)%2 for x in input().split()]
if sum(A) % 2 == 1:
    print("NO")
else:
    print("YES")