k, a, b = map(int, input().split())
print(k+1 + (k-a+1)//2 * max(0, b-a-2))