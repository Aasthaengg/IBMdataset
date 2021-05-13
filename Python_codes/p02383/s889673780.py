dice = {'N':(2, 6, 3, 4, 1, 5),'E':(4, 2, 1, 6, 5, 3),'W':(3, 2, 6, 1, 5, 4),'S':(5, 1, 3, 4, 6, 2)}
num = input().split()
for alf in input():
    num = [num[i-1]for i in dice[alf]]
print(num[0])

