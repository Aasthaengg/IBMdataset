n = int(input())

def training(n):
    power = 1
    for i in range(1, n+1):
        power = power * i % 1000000007
    return power

print(training(n))