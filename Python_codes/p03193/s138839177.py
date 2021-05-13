data = input().split()

N = int(data[0])
H = int(data[1])
W = int(data[2])

A = []
B = []
count = 0

for i in range(N):
    a_b_data = input().split()
    A.append(int(a_b_data[0]))
    B.append(int(a_b_data[1]))
    
for j in range(N):
    if H <= A[j] and W <= B[j]:
        count = count + 1
        
print(count)