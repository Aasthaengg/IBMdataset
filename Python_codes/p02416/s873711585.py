# coding: utf-8
# Here your code !
 
def func():
    inputdata=[]
    while(True):
        try:
            line=input().rstrip()
            if(int(line)==0):
                break
            else:
                inputdata.append(line)
        except EOFError:
            return 0
        except:
            return inputError()
    
    data=[sum( [int(char) for char in item] ) for item in inputdata]
    [print(item) for item in data]
        
def inputError():
    print("input Error")
    return -1
 
func()