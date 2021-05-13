n, q = map(int, input().split())
input_list = []
for i in range(n):
    name, time = input().split()
    input_list.append([str(name), int(time)])
queue_head = 0
now_time = 0
while queue_head != len(input_list):
    if q < input_list[queue_head][1]:
        input_list.append([input_list[queue_head][0], input_list[queue_head][1] - q])
        queue_head += 1
        now_time += q
    else:
        now_time += input_list[queue_head][1]
        print(input_list[queue_head][0], now_time)
        queue_head += 1

