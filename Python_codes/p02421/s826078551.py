Pt = 0
Ph = 0

n = int(input())

for i in range(n):
    I = input().split()
    Taro = I[0]
    Hanako = I[1]
    if Taro > Hanako:
        Pt += 3
    if Taro < Hanako:
        Ph += 3
    if Taro == Hanako:
        Pt += 1
        Ph += 1

print(str(Pt) + ' ' + str(Ph))