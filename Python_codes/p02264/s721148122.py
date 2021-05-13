class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

queue = []

[n, q] = list(map(int, input().split()))

for i in range(n):
    [name, str_time] = input().split()
    time = int(str_time)
    queue.insert(0, Task(name, time))


elps = 0

while queue != []:
    one = queue.pop()
    a = min(one.time, q)
    one.time -= a
    elps += a
    if one.time > 0:
        queue.insert(0, one)
    else:
        print(one.name, elps)