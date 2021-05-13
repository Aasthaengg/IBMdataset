# coding: utf-8
# Here your code !

def func():
    try:
        ringstr=input().rstrip()
        instr=input().rstrip()
    except:
        return inputError()

    while(True):
        ringstr+=ringstr
        if(len(ringstr) >= len(instr)*2):
            break
    
    print("Yes" if (instr in ringstr) else "No")

def inputError():
    print("input Error")
    return -1
 
func()