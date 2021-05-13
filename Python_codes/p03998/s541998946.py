A = list(input())
B = list(input())
C = list(input())

now = A.pop(0)
while True:
    if now == "a":
        if len(A) == 0:
            print("A")
            exit()
        now = A.pop(0)
        
    elif now == "b":
        if len(B) == 0:
            print("B")
            exit()
        now = B.pop(0)
        
    else:
        if len(C) == 0:
            print("C")
            exit()
        now =C.pop(0)