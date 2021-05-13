class Process:
    def __init__(self, process_name, process_time):
        self.name = process_name
        self.time = process_time
        self.remaing_time = process_time
        self.complete_flg = False

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_remaining_time(self):
        return self.remaing_time

    def exec_process(self, quantum):
        if self.remaing_time <= quantum:
            self.complete_flg = True
            use_time = self.remaing_time
            self.remaing_time = 0
            return use_time
        else:
            self.remaing_time -= quantum
            return quantum

    def get_complete_flg(self):
        return self.complete_flg

if __name__ == '__main__':
    n, q = [int(x) for x in input().split()]
    all_time = 0
    procesies = []
    for _ in range(n):
        name, time = input().split()
        temp_process = Process(name, int(time))
        procesies.append(temp_process)

    while len(procesies) != 0:
        target_process = procesies.pop(0)
        all_time += target_process.exec_process(q)
        if target_process.get_complete_flg():
            print(target_process.get_name() + " " + str(all_time))
        else:
            procesies.append(target_process)

