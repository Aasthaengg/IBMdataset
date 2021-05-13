n=int(input())
task_list=[]
for i in range(n):
    task_list.append([int(x) for x in input().split()])
import operator
task_list.sort(key=operator.itemgetter(1))
time_now=0
for i in range(n):
    time_now+=task_list[i][0]
    if time_now>task_list[i][1]:
        print("No")
        exit()
    
print("Yes")