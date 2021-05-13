# coding: utf-8
class CPU():
    def __init__(self, in_quantum):
        self.quantum = in_quantum
        self.total_time = 0
        
    def deal(self, in_process, in_time):
        sum_process_time = 0
        this_process_time = 0

        sum_process_time += in_time[0]
        
        if sum_process_time > self.quantum:
            remain_time = sum_process_time - self.quantum
            this_process_time = in_time[0] - remain_time
            sum_process_time = self.quantum
        
            in_process.append(in_process[0])
            in_time.append(remain_time)
            
            self.total_time += this_process_time
        else:
            this_process_time = in_time[0]
            self.total_time += this_process_time
            #make log
            self.makeLog(in_process[0])

        in_process.pop(0)
        in_time.pop(0)
        
        return in_process, in_time

    def makeLog(self, in_process):
        print(in_process, self.total_time)

    
processes = []
times = []
    
data_cnt, quantum =  list(map(int,input().split(" ")))  

for i in range(data_cnt):
    tmp_process, tmp_time = input().split(" ")
    processes.append(tmp_process)
    times.append(int(tmp_time))

objCPU = CPU(quantum)

while True:
    processes, times = objCPU.deal(processes, times)

    if len(processes) == 0:
        break