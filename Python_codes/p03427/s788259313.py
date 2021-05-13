N = input()
if len(N) == 1 or N[1:len(N)].count('9') == len(N)-1:
    print(sum([int(i) for i in N]))
else :
    print(int(N[0])-1+9*(len(N)-1))
