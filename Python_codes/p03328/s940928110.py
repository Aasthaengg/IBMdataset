def total_n(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

a, b = map(int, input().split())
print(total_n(b-a)-b)