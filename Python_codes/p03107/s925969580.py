S=list(map(int, list(input())))

num1 = sum(S)
num0 = len(S) - num1

print(min(num1,num0)*2)