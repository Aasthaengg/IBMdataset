A, B = [int(input()), int(input())]

#  Pythonのintは無限長なので勝ち

if A > B:
    print("GREATER")
elif A == B:
    print("EQUAL")
else:
    print("LESS")