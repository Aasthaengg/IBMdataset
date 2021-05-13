n = int(input())
s = input()
white = s.count(".")
black = s.count("#")

min_num = min(black, white)
black_num = 0
for i, color in enumerate(s, start = 1):
    if color == "#":
        black_num += 1
    min_num = min(min_num, black_num + white - (i - black_num))
    
print(min_num)