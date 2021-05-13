n = int(input())
l = [int(i) for i in input().split()]
m = max(l)
print("Yes" if sum(l)-m > m else "No")