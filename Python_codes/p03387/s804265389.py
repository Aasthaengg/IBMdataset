ABC = list(map(int, input().split()))

ABC.sort(reverse = True)

step1 = ABC[0] - ABC[1]
step2 = ABC[0] - ABC[2] - step1

if step2 % 2 == 0:
    result  = int(step2 / 2) + step1
else:
    result = int(step2 / 2) + step1 + 2
print(result)