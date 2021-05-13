n = int(input())
arr = []
for i in range(n):
    c = input()
    arr.append(c)
    
di = {"AC":0,"WA":0,"TLE":0,"RE":0}

for i in arr:
    if i in di:
        di[i] += 1 
    else:
        di[i] = 1 
        
print("AC x " + str(di.get("AC")))
print("WA x " + str(di.get("WA")))
print("TLE x " + str(di.get("TLE")))
print("RE x " + str(di.get("RE")))