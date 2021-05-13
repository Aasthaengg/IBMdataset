k = int(input())
a, b = map(int, input().split())
i = 0
while k*i < a:
    i = i + 1
print("OK" if k*i <= b else "NG")