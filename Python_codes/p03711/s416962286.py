l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [4, 6, 9, 11]

x, y = map(int, input().split())
flg = x in l1 and y in l1 or x in l2 and y in l2
print("Yes" if flg else "No")