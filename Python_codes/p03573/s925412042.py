S_list = list(map(int,input().split()))

#S = input("入力：")
#S_list = S.split()
A, B, C= S_list[0], S_list[1], S_list[2]
AB, BC, CA = A-B, B-C, C-A
if AB*BC !=0 :
    print(B)
elif CA*AB !=0 :
    print(A)
else:
    print (C)
