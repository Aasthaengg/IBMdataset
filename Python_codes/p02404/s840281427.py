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
            if( (i==0) or (i==height-1) ):
                result+="#"*width+"\n"
            elif(width<3):
                result+="#"*width+"\n"
            else:
                result+="#"+"."*(width-2)+"#\n"
        result+="\n"
    
    print(result[:-1])
        
def inputError():
    print("input Error")
    return -1
 
func()