n = int(input())
a_list = list(map(int, input().split()))
a_list_0 = [0] + a_list + [0]
s = sum([abs(a_list_0[i + 1] - a_list_0[i]) for i in range(n + 1)])
for i in range(1, n + 1):
    note = s - (abs(a_list_0[i] - a_list_0[i - 1]) + abs(a_list_0[i] - a_list_0[i + 1]))
    note += abs(a_list_0[i + 1] - a_list_0[i - 1])
    print(note)