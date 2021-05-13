# coding: utf-8
# Here your code !
 
def func():
    result=""
    while(True):
        try:
            line = input().rstrip()
            numbers = line.split(" ")
            for i,item in enumerate(numbers):
                numbers[i]=int(item)
        except:
            print("input error")
            return -1
         
        if( (numbers[0] > 0) and (numbers[1] > 0) ):
            for i in range(numbers[0]):
                result += "#"*numbers[1]+"\n"
            result += "\n"
        elif( (numbers[0] == 0) and (numbers[1] == 0) ):
            break
        else:
            print("input error")
            return -1
             
    print(result[:-1])
 
func()