n = int(input())
t = list(map(int,input().split()))
sum_t = sum(t)
T_all = []
for i in range(int(input())):
    T = sum_t
    p,x = map(int,input().split())
    T += (x-t[p-1])
    T_all.append(T)

for j in range(len(T_all)):
    print(T_all[j])