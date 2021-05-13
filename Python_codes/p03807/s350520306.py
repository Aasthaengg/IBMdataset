n = int(input())
a = [int(i) % 2 for i in input().split()]
print("NO") if sum(a) % 2 else print("YES")