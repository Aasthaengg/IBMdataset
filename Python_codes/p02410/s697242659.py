x,y = map(int,input().split(" "))

line_1 = [[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
	line_1[i] = list(map(int,input().split(" ")))

line_2 = [int(input()) for _ in range(y) ]

[print(sum([line_1[k][m] * line_2[m] for m in range(y)])) for k in range(x)]

