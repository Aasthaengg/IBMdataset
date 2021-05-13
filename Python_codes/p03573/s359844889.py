##### 解けた #####

A,B,C=input().split(" ")

if A==B: # Cが仲間外れの場合
    print(C)
elif A==C: # Bが仲間外れの場合
    print(B)
elif B==C: # Aが仲間外れの場合
    print(A)