a, b, c = map(int, input().split())

bell_1 = a + b
bell_2 = b + c
bell_3 = c + a

if (bell_1 <= bell_2) and (bell_1 <= bell_3):
    print(bell_1)

elif (bell_2 <= bell_1) and (bell_2 <= bell_3):
    print(bell_2)

elif (bell_3 <= bell_1) and (bell_3 <= bell_2):
    print(bell_3)
    
