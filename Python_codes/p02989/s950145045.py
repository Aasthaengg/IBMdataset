n = int(input())
a = list(map(int,input().split(" ")))
b = sorted(a)
print(b[n//2] - b[(n//2) - 1])