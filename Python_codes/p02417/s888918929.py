# coding: utf-8
# Here your code !
 
from collections import Counter
 
def func():
    inputdata=""
    while(True):
        try:
            line=input()
            inputdata+=line
        except EOFError:
                break
        except:
            return inputError()

    alphabets_small=[ chr(i) for i in range(97,97+26) ]

    counter=Counter(inputdata.lower())
    data=dict(counter)

    for char in alphabets_small:
        try:
            print(char+" : "+str(data[char]))
        except:
            print(char+" : 0")
    

def inputError():
    print("input Error")
    return -1
 
func()