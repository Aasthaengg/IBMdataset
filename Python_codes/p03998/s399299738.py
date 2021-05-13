A = list(input())
B = list(input())
C = list(input())
current_state = A.pop(0)

while True:
    if current_state == 'a':
        if len(A) == 0:
            print(current_state.upper())
            exit()
        
        current_state = A.pop(0)

    if current_state == 'b':
        if len(B) == 0:
            print(current_state.upper())
            exit()
        
        current_state = B.pop(0)
        
    if current_state == 'c':
        if len(C) == 0:
            print(current_state.upper())
            exit()
        
        current_state = C.pop(0)

