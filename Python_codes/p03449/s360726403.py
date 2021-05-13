N = int(input())

A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))

can_list=[]

for i in range(N) :
    A_1_can = sum(A_1[0:i+1])
    A_2_can = sum(A_2[i:N])

    can_list.append(A_1_can+A_2_can)

print(max(can_list))
