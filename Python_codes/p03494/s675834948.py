N = int(input())  # nは入力回数
num_list =  list(map(int, input().split()))
    
count = 0
actual_count = 0
w = 0
new_list = []
while (w == 0):
    count = 0
    for i in range(N):
        a = num_list[i]
        
        b = int(a) % 2 
        if (b == 0):
            count = count + 1
    if (count == N):
            new_list =[]
            for n in range(N):
                a = num_list[n]
                b = int(a) / 2
                new_list.append(b)
            num_list = []
            for l in range(N):
                a = new_list[l]
                num_list.append(a)
                
            
            actual_count += 1
    else:
        w = 1
        
        
print(actual_count)