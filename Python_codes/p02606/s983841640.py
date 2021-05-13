li = list(map(int, input().split()))
result = int(li[1]/li[2]) - int(li[0]/li[2])
if li[0] % li[2] == 0:
    result += 1
print(result)
