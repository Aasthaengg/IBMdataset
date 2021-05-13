#coding: utf-8

def factoraization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if (temp != 1):
        arr.append([n, 1])
    
    return arr
    
if __name__ == '__main__':
    N = int(input())
    
    num_lst = []
    for i in range(1, N + 1, 2):
        num_lst.append(i)
        
    result = 0
    
    for j in num_lst:
        
        count = 1
        x = factoraization(j)

        for t in range(len(x)):
            count *= (int(x[t][1]) + 1)
            
            if count == 8:
                result += 1
    
    print(result)