A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())


def ball(b):
    global A
    for c in range(3):
        for co in range(3):
            if A[c][co] == b:
                A[c][co] = "ok"


for c in range(N):
    b = int(input())
    ball(b)


if A[0].count("ok") == 3 or A[1].count("ok") == 3 or A[2].count("ok") == 3:
    print("Yes")
elif A[0][0] == "ok" and A[1][0] == "ok" and A[2][0] == "ok":
    print("Yes")
elif A[0][1] == "ok" and A[1][1] == "ok" and A[2][1] == "ok":
    print("Yes")
elif A[0][2] == "ok" and A[1][2] == "ok" and A[2][2] == "ok":
    print("Yes")
elif A[0][0] == "ok" and A[1][1] == "ok" and A[2][2] == "ok":
    print("Yes")
elif A[0][2] == "ok" and A[1][1] == "ok" and A[2][0] == "ok":
    print("Yes")
else:
    print("No")
