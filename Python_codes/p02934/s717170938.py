N = int(input())
As = list(map(int, input().split()))
bunbo = 1
for i in As:
    bunbo *= i
bunshi_list = []
for i in As:
    bunshi_list.append(bunbo // i)
print(bunbo / sum(bunshi_list))