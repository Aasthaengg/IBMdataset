N = input().strip()
num=0

for i in range(len(N)):
    if N[i] == '2':
        num += 1
        
print(num)