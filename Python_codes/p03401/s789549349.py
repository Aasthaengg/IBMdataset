#92c
N = int(input()) #<=10**5
A_list = [0] + [int(e) for e in input().split()] + [0]

fare = [abs(A_list[i]-A_list[i-1]) for i in range(1,N+2)]
sum_fare = sum(fare)

#print(A_list)
#print(fare)

for i in range(1,N+1):
    print(sum_fare - (fare[i-1]+fare[i]) + abs(A_list[i+1] - A_list[i-1]))