def c167(x):
    if x[1][:-1] == x[0]: return "Yes"
    else: return "No"

    
if __name__=="__main__":
    input1 = input()
    input2 = input()
    input3 = [input1,input2]
    print(c167(input3))
