line = input()
n = int(input())
for i in range(n):
    order = input().split()
    if order[0] == "print":
        print(line[int(order[1]):int(order[2])+1])
    elif order[0] == "reverse":
        tmp = line[int(order[1]) :int(order[2])+1 ]
        line = line[:int(order[1])] + tmp[::-1] + line[int(order[2])+1:]
    elif order[0] == "replace":
        line = line[:int(order[1])] + order[3] + line[int(order[2])+1:]