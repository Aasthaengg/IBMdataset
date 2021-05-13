N = int(input())
D, X = map(int,input().split())

sum = 0
for i in range(N):
    a = int(input())
    d = 0
    i = 0
    while d <= D:
        d = a*i + 1
        i += 1
        if d <= D:
	        sum += 1

print(sum + X) 