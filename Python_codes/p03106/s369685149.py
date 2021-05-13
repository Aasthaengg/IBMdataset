a, b, k = map(int, input().split())
l = [i for i in range(1, min(a, b) + 1) if not (a % i or b % i)]
print(l[-k])
