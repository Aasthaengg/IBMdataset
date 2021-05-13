S = input()
T = input()
a = len(T)
new_S = S + T[a-1]
if new_S == T:
    print("Yes")
else:
    print("No")
