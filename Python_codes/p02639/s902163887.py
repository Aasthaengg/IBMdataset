user_input = list(map(int, input().split()))
# print(user_input)
# to find the index where zero is located
indexOfZero = [x for x in range(0, 5) if user_input[x] == 0]
print(indexOfZero[0] + 1)