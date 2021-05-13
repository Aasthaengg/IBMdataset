n = int(input())
l = [1 for i in input().split() if int(i)%2]
print("NO" if len(l)%2 else "YES")