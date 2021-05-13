n,c = map(int,input().split())
program = [list(map(int,input().split())) for i in range(n)]
time = [0 for i in range(10**5+1)]

program.sort()
program.sort(key = lambda x: x[2])
 
for i in range(1,n):
    if program[i][2]==program[i-1][2] and program[i][0]==program[i-1][1]:
        program[i][0] = program[i-1][0]
        program[i-1][0] = None
#print(program)
 
for i in range(n):
    if program[i][0] == None:
        continue
    time[program[i][0]-1] += 1
    time[program[i][1]] -= 1
 
count = 0
max_count = 0
 
for i in range(10**5+1):
    count += time[i]
    max_count = max(max_count,count)
 
print(max_count)