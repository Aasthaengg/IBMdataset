n = int(input())
t, a = map(int, input().split())
for i in range(n - 1):
    r1, r2 = map(int, input().split())
    if r1 >= t and r2 >= a:
        multiple = 1
    elif r1 < t and r2 >= a:
        multiple = (t-1) // r1 + 1
    elif r1 >= t and r2 < a:
        multiple = (a-1) // r2 + 1
    else:
        multiple = max((t-1) // r1, (a-1) // r2) + 1
    t, a = r1 * multiple, r2 * multiple
print(t+a)