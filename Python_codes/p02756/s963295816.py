S = input()
T = ""
B = ""
f = 1
for _ in range(int(input())):
    L = list(input().split())
    if L[0] == "1":
        f *= -1
    else:
        if f == 1:
            if L[1] == "1":
                T += L[2]
            else:
                B += L[2]
        else:
            if L[1] == "1":
                B += L[2]
            else:
                T += L[2]

if f == 1:
    print(T[::-1]+S+B)
else:
    print(B[::-1]+S[::-1]+T)
