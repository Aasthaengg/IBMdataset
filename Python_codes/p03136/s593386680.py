input()
a = list(map(int,input().split()))
b = sorted(a)
print("Yes" if b[-1] < (sum(b)-b[-1]) else "No")