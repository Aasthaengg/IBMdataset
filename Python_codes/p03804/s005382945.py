import numpy as np
N, M = 3, 2

ARR = [
    list("#.#"),
    list(".#."),
    list("#.#"),
]

ARR2 = [
    "#.",
    ".#"
]


#
#
# N,M = 4, 1
# ARR = [
#     "....",
#     "....",
#     "....",
#     "....",
# ]
#
# ARR2 = [
#     "#"
# ]
# #
# N,M = 5,2
#
# ARR = [
#     "...##.",
#     "###..#",
#     "...##.",
#     "......",
#     "....##"
# ]
#
# ARR2 = [
#     "......",
#     "....##"
# ]
#
N,M = map(int,input().split())
ARR = []

for i in range(N):
    ARR.append(list(input()))

ARR2 = []

for j in range(M):
    ARR2.append(input())


def calculate(n, m, arr1, arr2):
    arr1 = np.array(arr1)
    isOK = False
    for j in range(0, n - m + 1):
        for i in range(0, len(arr1[0]) - len(arr2[0]) + 1):
            # print(j, i)
            c1 = arr1[j:j + m,i:i + len(arr2[0])]
            s1 = np.ravel(c1)
            s1 = "".join(s1)
            s2 = "".join(arr2)
            if s1 == s2:
                isOK = True
                break

        if isOK == True:
            break

    if isOK:
        print("Yes")
    else:
        print("No")


calculate(N, M, ARR, ARR2)
