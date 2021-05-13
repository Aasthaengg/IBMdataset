N=int(input())
L_0 = 2
L_1 = 1
if N==0:
    print(L_0)
elif N==1:
    print(L_1)
else:
    for i in range (N-2):
        if i%2 ==0:
            L_0 = L_0 + L_1
        else:
            L_1 = L_0 + L_1
    print(L_0 + L_1)
