lst = input().split()
ab = list(map(int, input().split()))
ab[lst.index(input())] -= 1
print(str(ab[0]) + ' ' + str(ab[1]))