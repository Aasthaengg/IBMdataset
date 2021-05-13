n = int(input())

passenger = []
for i in range(5):
    passenger.append(int(input()))
    
minimum = min(passenger)

ans = -(-n//minimum)

print(ans+4)