n = int(input())
t, a = list(map(int, input().split()))
h_list = list(map(int, input().split()))

def temp(x):
    y = abs(t - x*0.006 - a)
    return y
t_dif = list(map(temp, h_list))
t_min = min(t_dif)
t_index = int(t_dif.index(t_min))
print(t_index+1)