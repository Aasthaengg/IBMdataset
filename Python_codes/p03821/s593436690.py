import math

N = int(input())

A_list = list()
B_list = list()
A_list.append(0)
B_list.append(0)

for i in range(N):
    A,B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

#末尾から考える
ans = 0
for i in range(N):
    A = A_list.pop(-1)
    B = B_list.pop(-1)
    #print(A,B,"→",end="")
    A += ans
    goal = B*math.ceil(A/B)
    #print(":",goal)
    ans += goal - A
    
print(ans)