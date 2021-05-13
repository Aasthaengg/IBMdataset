
n = int(input())
aoki, takahashi = [], []
for i in range(n):
    t, a = [ int(v) for v in input().split() ]
    aoki.append((-t-a, -a, i))
    takahashi.append((-a-t, -t, i))
dish_list = [1] * n
aoki.sort(), takahashi.sort()

a_score, t_score = 0, 0
a_counter, t_counter = 0, 0
for i in range(n):
    stop = 0
    if i % 2 == 0:
        while not stop:
            if dish_list[takahashi[t_counter][2]] == 1:
                t_score -= takahashi[t_counter][1]
                dish_list[takahashi[t_counter][2]] = 0
                stop = 1
            t_counter += 1
    else:
        while not stop:
            if dish_list[aoki[a_counter][2]] == 1:
                a_score -= aoki[a_counter][1]
                dish_list[aoki[a_counter][2]] = 0
                stop = 1
            a_counter += 1
print(t_score - a_score)