N = int(input())
seat = []
for i in range(N):
    seat.append(input().split())

con = 0
for j in range(N):
    con += int(seat[j][1]) - int(seat[j][0]) + 1

print(con)