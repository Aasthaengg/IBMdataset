#A,B,C,D=map(int, list(input()))
numbers = list(map(int, list(input())))
seven="=7"

for i in range(1<<3):
    pms = []
    for j in range(3):
        if (i>>j)&1:
            pms.append(1)
        else:
            pms.append(0)
    result = numbers[0]
    result_str = str(numbers[0])
    for j, pm in enumerate(pms):
        j+=1
        if pm:
            result+=numbers[j]
            result_str+="+%d"%(numbers[j])
        else:
            result-=numbers[j]
            result_str+="-%d"%(numbers[j])
    if result==7:
        print(result_str+seven)
        break
