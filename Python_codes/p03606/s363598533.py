n = int(input())
seats = []
for i in range(n):
    l, r = map(int, input().split())
    seat = r - l +1
    seats.append(seat)
print(sum(seats))