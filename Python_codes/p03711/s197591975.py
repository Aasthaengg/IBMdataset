o = [2]
t = [4, 6, 9, 11]
ttt = [1, 3, 5, 7, 8, 10, 12]
x, y = map(int, input().split())
if x in o and y in o:
    print("Yes")
elif x in t and y in t:
    print("Yes")
elif x in ttt and y in ttt:
    print("Yes")
else:
    print("No")