A = int(input())
B = int(input())

s1 = {1, 2, 3}
s2 = set()
s2.add(A)
s2.add(B)
for i in s1 - s2:
    print(i)