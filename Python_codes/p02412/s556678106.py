count = []

while True:
    sub_count = 0
    n,x = map(int,raw_input().split())
    if n == x == 0:
        break
    
    for i in range(n):
       for j in range(n):
           for k in range(n):
               if ((i + j + k + 3) == x) and ((i != j != k != i) == True):
                   sub_count += 1
    count.append((sub_count / 6))


for i in range(len(count)):
    print count[i]