# coding: utf-8
# Here your code !
 
def func():
    data=[]
    while(True):
        try:
            [height,width] = [ int(item) for item in input().rstrip().split(" ") ]
        except:
            return inputError()
         
        if( (height > 0) and (width > 0) ):
            data.append([height,width])
        elif( (height == 0) and (width == 0) ):
            break
        else:
            return inputError()
    
    result=""
    for item in data:
        [height,width]=item
        for i in range(height):
            for j in range(width):
                strfunc = lambda x : "#" if x%2==0 else "."
                result+=strfunc(i+j)
            result+="\n"
        result+="\n"
    print(result[:-1])
        
def inputError():
    print("input Error")
    return -1
 
func()