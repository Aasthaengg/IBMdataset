n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]

ab = sorted(ab, key=lambda x:(x[1], -x[0]))
count = 0
for i in range(n):
    count += ab[i][0]
    if count > ab[i][1]:
        print("No")
        break
else:
    print("Yes")    