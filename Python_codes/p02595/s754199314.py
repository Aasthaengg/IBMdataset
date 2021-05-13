n, d = map(int, input().split())
lst =[list(map(int,input().split())) for i in range(n)]

count = 0

for lst_i in lst:
    if lst_i[0]**2 + lst_i[1]**2 <= d**2:
        count += 1

print(count)