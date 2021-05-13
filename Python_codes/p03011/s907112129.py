P, Q, R = map(int, input().split())
#3つの中で1,2番目に小さい数の和
flight_time = [P, Q, R]
flight_time.sort()
answer =flight_time[0] + flight_time[1]
print(answer)