n = int(input())
l = list(map(int, input().split()))
l.sort()
print(abs(l[n//2-1] - l[n//2]))