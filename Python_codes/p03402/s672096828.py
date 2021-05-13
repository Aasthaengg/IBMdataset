def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


A, B = readmap()

print(100, 100)

arr = [["."] * 50 + ["#"] * 50 for _ in range(100)]

for a in range(1, A):
    arr[2 * (a // 20) + 1][2 * (a % 20) + 51] = "."

for b in range(1, B):
    arr[2 * (b // 20) + 1][2 * (b % 20) + 1] = "#"

for i in range(100):
    print("".join(arr[i]))