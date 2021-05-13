n, d = list(map(int, input().split()))
fov = 2 * d + 1
print(n // fov if n % fov == 0 else (n // fov) + 1)