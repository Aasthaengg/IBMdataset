x,y,z = map(int,input().split())
box_A = [x]
box_B = [y]
box_C = [z]

box_B.append(box_A.pop(0))
box_A.append(box_B.pop(0))
box_A.append(box_C.pop(0))
box_C.append(box_A.pop(0))
print(box_A[0],box_B[0],box_C[0])


#1 2 3
#100 100 100
#41 59 31