# solution

nim, mike = map(int, input().split())
print(mike * (mike - 1) ** (nim - 1))