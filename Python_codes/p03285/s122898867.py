N = int(input())

"""
4k = N - 7n
"""
for i in range(15):
    k = (N-(7*i)) / 4
    if k % 1 == 0 and k >= 0:
        print("Yes")
        break
    if i == 14:
        print("No")