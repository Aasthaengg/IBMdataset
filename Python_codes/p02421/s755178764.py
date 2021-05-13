n = int(input())
T_point = 0
H_point = 0
for loop in range(n):
    T,H=map(str,input().split())
    if T > H:T_point += 3
    elif T == H:
        T_point += 1
        H_point += 1
    else:H_point += 3
print(T_point,H_point)
