# coding: utf-8
# Here your code !

def func():
        try:
            nums = input()
            line = input().rstrip()
            numbers = line.split(" ")
            for i,item in enumerate(numbers):
                numbers[i]=int(item)
        except:
            print("input error")
            return -1
        
        print(str(min(numbers))+" "+str(max(numbers))+" "+str(sum(numbers)))
        

func()