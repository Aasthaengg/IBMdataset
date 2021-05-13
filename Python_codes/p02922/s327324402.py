#B-powersocket
A, B = map(int, input().split())
A -= 1
B -= 1

if B % A == 0:
    print (B // A)
else:
    print(B // A + 1)

  