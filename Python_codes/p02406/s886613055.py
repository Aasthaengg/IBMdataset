# coding: utf-8
# Here your code !

def func():
    result=""
    try:
        line = input().rstrip()
        num = int(line)
    except:
        print("input error")
        return -1
        
    for i in range(1,num+1):
        if(i % 3 ==0):
            result += " "+str(i)
        else:
            devided=i
            while(True):
                if(devided % 10 == 3):
                    result += " "+str(i)
                    break
                elif(devided > 9):
                    devided = devided // 10
                else:
                    break
                
    print(result)

func()