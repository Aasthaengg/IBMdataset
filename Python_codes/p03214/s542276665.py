N = int(input())
As = list(map(int, input().split()))
s = sum(As)
r = min(range(N), key=lambda i: abs(N*As[i]-s))
print(r)
