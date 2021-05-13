S = input()
num = ""
l = len(S)
dis = float("inf") 

for i in range(l-2):
    num = S[i:i+3]
    if abs(753-int(num)) < dis:
        dis = abs(753-int(num))
        
print(dis)