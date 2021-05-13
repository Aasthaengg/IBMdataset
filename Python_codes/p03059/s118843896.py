#スペース区切りスペース区切りの整数を受け取る
a, b, t = list(map(int, input().strip().split()))
print((t // a) * b)
