def PalindJudge(num):
    
    judge = 1
    list = [0,0,0,0,0]
    
    for i in range(5):
        list[i] = num%10
        num //= 10
        
    for i in range(3):
        if list[i]!=list[4-i]:
            judge *= 0
            
    return judge

if __name__ == '__main__':
    
    a,b = map(int, input().split())
    
    count = 0
    
    for i in range(a, b+1):
        if PalindJudge(i) == 1:
            count += 1
            
    print(count)