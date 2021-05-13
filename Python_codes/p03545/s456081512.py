tmp=input()
solution=7
numbers=[]
for i in range(len(tmp)):
    numbers.append(int(tmp[i]))

n = len(numbers)
for i in range(n ** 2):
    ops = ["-"] * (n-1)
    for j in range(n-1):
        if ((i>>j) & 1):
            ops[n-1-j-1]="+"
    #print(ops)
    shiki = str(numbers[0])
    for j in range(n-1):
        shiki = shiki + ops[j] + str(numbers[j+1])
    #print(shiki)
    if int(eval(shiki)) == int(solution):
        print(shiki+"="+str(solution))
        break
