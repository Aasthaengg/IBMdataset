def calc_temp(x,T):
    return T - x * 0.006

N = int(input())
T,A = map(int,input().split())
H_list = list(map(int,input().split()))

near_temp = 1000

for i in range(N):
    if abs(A - calc_temp(H_list[i],T)) <= abs(A - near_temp):
        near_temp = calc_temp(H_list[i],T)
        num = i+1

print(num)