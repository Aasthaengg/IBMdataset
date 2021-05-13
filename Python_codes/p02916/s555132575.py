N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev_dish = -1
satisfaction = 0
for dish in A:
    satisfaction += B[dish-1]
    if dish - prev_dish == 1:
        satisfaction += C[prev_dish-1]
    
    prev_dish = dish

print(satisfaction)
