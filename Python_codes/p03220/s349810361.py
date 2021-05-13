n = int(input())
t, a = map(int, input().split())
list = [int(i) for i in input().split()]

dif_list = []
answer = 0

for i in range(n):
    t_i = t - list[i] * 0.006
    t_i_dif = abs(a - t_i)
    dif_list.append(t_i_dif)
    if min(dif_list) == t_i_dif:
        answer = i + 1

print(answer)
