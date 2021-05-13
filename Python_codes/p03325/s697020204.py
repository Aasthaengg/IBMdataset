N = int(input())
#10
a = [int(i) for i in input().split()]
#2184 2126 1721 1800 1024 2528 3360 1945 1280 1776

ans = 0
sm = 0
for aa in a:
	t = aa
	while t % 2 == 0:
		t = t // 2
		sm += 1

print(sm)
