time = list(int(input()) for i in range(5))

def f(x):
    return (10-x%10)%10

b = list(map(f, time))

ans = sum(time) + sum(b) - max(b)
print(ans)
