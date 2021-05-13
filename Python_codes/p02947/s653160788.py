N = 3
SRR = [
    "acornistnt",
    "peanutbomb",
    "constraint",
]

N = 5
SRR = [
    "abaaaaaaaa",
    "oneplustwo",
    "aaaaaaaaba",
    "twoplusone",
    "aaaabaaaaa",
]

N = int(input())
SRR = []

for i in range(N):
    SRR.append(input())

def calculate(n,arr):
    dict = {}
    for i in range(n):
        str = "".join(sorted(list(arr[i])))
        if dict.get(str) == None:
            dict.__setitem__(str,1)
        else:
            dict.__setitem__(str,dict.get(str) + 1)

    result = 0

    for item in dict.values():
        if item > 1:
            result += (item * (item-1)) // 2

    print(result)


calculate(N, SRR)