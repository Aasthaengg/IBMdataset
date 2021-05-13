s = list(input())

check = list("CODEFESTIVAL2016")
cnt = 0

for x,y in zip(s,check):
    if x != y:
        cnt += 1
        
print(cnt)