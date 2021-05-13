str = input()
str_list = list(str)
q = int(input())
for i in range(q):
    order = input().split()
    if order[0] == 'print':
        for i in range(int(order[1]),int(order[2])+1):
            print("{}".format(str_list[i]),end=(''))
        print('')
    elif order[0] == 'replace':
        word=list(order[3])
        j = 0
        for i in range(int(order[1]),int(order[2])+1):
            str_list[i]=word[j]
            j = j + 1
    elif order[0] == 'reverse':
        word = list(str_list[int(order[1]):int(order[2])+1])
        j = len(word)
        for i in range(int(order[1]),int(order[2])+1):
            str_list[i] = word[j-1]
            j = j - 1      
