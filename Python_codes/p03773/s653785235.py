A, B = map(int, input().split())
hours = [i for i in range(24)]
res = hours[(A+B)%24]
print(res)