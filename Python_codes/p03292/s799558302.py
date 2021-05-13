a1, a2, a3 = map(int, input().split())
if (a1 <= a2 and a2 <= a3) or (a3 <= a2 and a2 <= a1):
    print(abs(a2 - a1) + abs(a3 - a2))
elif (a2 <= a1 and a1 <= a3) or (a3 <= a1 and a1 <= a2):
    print(abs(a1 - a2) + abs(a3 - a1))
else:
    print(abs(a3 - a1) + abs(a2 - a3))