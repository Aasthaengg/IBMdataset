ProNum = int(input())
time = input()
time = (time.split())
TotalTime = 0

for t in time:
  TotalTime += int(t)
                  
DrinkNum = int(input())

for d in range(DrinkNum):
  line = input()
  line = line.split()
  diff = int(line[1]) - int(time[int(line[0])-1])
  print(TotalTime+diff)