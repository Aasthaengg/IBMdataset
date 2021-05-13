A, B = map(int, input().split())
T = [["#"] * 100 for i in range(100)]
for i in range(50, 100):
    T[i] = ["."] * 100

A -= 1
for i in range(50):
    if A == 0:
        break
    if i % 2 == 0:
        for j in range(100):
            if j % 2 == 0:
                T[i][j] = "."
                A -= 1
                if A == 0:
                    break

B -= 1
for i in range(51, 100):
    if B == 0:
        break
    if i % 2 != 0:
        for j in range(100):
            if j % 2 == 0:
                T[i][j] = "#"
                B -= 1
                if B == 0:
                    break

print(100, 100)
for i in range(100):
    print("".join(T[i]))