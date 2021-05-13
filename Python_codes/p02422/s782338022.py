string = str(input())
q = int(input())
for _ in range(q):
    
    data = input().split()
    left = int(data[1])
    right = int(data[2]) + 1
    
    if data[0] == "print":
        print(string[left:right])
        
    elif data[0] == "reverse":
        string = string[:left] + string[left:right][::-1] + string[right:]
        
    else:
        string = string[:left] + data[3] + string[right:]

