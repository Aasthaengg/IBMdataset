# coding: utf-8
# Here your code !
 
def func():
    try:
        line=input().rstrip()
    except EOFError:
        return 0
    except:
        return inputError()

    print(line.swapcase())
        
def inputError():
    print("input Error")
    return -1
 
func()