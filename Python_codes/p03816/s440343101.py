n = int(input())
a_i = list(map(int, input().split()))
duplicationCheckList = [0] * 10 ** 5
duplicationMaisuu = 0
for x in a_i:
    if duplicationCheckList[x - 1] == 1: duplicationMaisuu += 1
    else: duplicationCheckList[x - 1] = 1
count = (duplicationMaisuu + 1) // 2
print(n - count * 2)