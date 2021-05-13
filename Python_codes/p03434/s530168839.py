N = int(input())
A = [int(x) for x in input().split()]
A.sort()
a, b, turn = 0, 0, 1
while len(A) != 0:
    if turn & 1:
        a += A.pop()
    else:
        b += A.pop()
    turn += 1
print(a-b)