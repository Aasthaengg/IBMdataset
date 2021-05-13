# input
ABC = list(map(int, input().split()))

# check
ABC.sort(reverse=True)
X = 10 * ABC[0] + ABC[1]
Y = ABC[2]
print(X + Y)