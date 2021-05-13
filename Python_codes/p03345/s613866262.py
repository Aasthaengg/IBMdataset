A,B,C,K = map(int,input().split())
s1 = 0
s2 = 0
for i in range(2):
    a = A + 2 * B
    b = B + 2 * A
    A = a
    B = b
    if i == 0:
        s1 = A - B
    else:
        s2 = A - B
if K % 2 == 1:
    if s1 < 10 ** 18:
        print(s1)
    else:
        print("Unfair")
else:
    if s2 < 10 ** 18:
        print(s2)
    else:
        print("Unfair")

