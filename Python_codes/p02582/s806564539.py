# string
# a, b, c = input().split()
# str_list = list(input().split())

# number
# a, b, c = map(int, input().split())
# num_list = list(map(int, input().split()))

# lows
# str_list = [input() for _ in range(n)]

# many inputs
# num_list = []
# for i in range(n): num_list.append(list(map(int, input().split())))

s = input()
if s[0] == "R":
    if s[1] == "R":
        if s[2] == "R":
            print(3)
        else:
            print(2)
    else:
        print(1)
else:
    if s[1] == "R":
        if s[2] == "R":
            print(2)
        else:
            print(1)
    else:
        if s[2] == "R":
            print(1)
        else:
            print(0)