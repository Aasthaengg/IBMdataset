N = input()

s = sum(int(x) for x in N)
if s % 9 == 0:
    print("Yes")
else:
    print("No")