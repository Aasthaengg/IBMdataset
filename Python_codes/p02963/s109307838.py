s = int(input())

div = s // 10**9
mod = s % 10**9
if mod == 0:
    print(0, 0, 10**9, 1, 0, div)
else:
    print(0, 0, 10**9, 1, 10 ** 9 - mod, div + 1)