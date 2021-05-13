N = int(input())
s = 0

for i in range(1, 10):
    for j in range(1, 10):

        if N == i * j:
            s = 1
if s == 1:
    print("Yes")
else:
    print("No")