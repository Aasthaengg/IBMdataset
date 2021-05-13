h, w = list(map(int, input().split()))
hw_list = [input() for _ in range(h)]

top = "#" * (w + 2)
print(top)
for hw in hw_list:
    print("#", end="")
    print(hw, end="")
    print("#")
print(top)
