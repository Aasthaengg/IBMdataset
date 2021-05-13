H =input()

count = 0
while(int(H)>1):
    H = int(H)/2
    count = count + 1

answer = 0
for i in range(count+1):
    answer = answer + 2 ** i
print(answer)