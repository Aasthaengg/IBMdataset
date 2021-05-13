argList = list(map(int, input().split())) 

n = argList[0]
m = argList[1]

citys = [0]*n

for i in range(m):
    arg = list(map(int, input().split())) 
    citys[arg[0]-1] +=1 
    citys[arg[1]-1] +=1 

for c in citys:
    print(c)