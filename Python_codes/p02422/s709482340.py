string = list(input())
n = int(input())

for repeat in range(n):
    ope = input().split()

    if ope[0] == "replace":
        rep_str = list(ope[3])
        rep_ind = 0
        #print(rep_str)
        for i in range(int(ope[1]), int(ope[2])+1):
            #print(string[i],rep_str[rep_ind])
            string[i] = rep_str[rep_ind]
            rep_ind += 1
        #print(string)
        
    elif ope[0] == "reverse":
        rev_str = []
        rev_ind = int(ope[2])
        times = 0
        for i in range(len(string)):
            rev_str.append(string[i])
        for i in range(int(ope[1]),int(ope[2])+1):
            string[i] = rev_str[rev_ind]
            rev_ind -= 1
        
    elif ope[0] == "print":
        for i in range(int(ope[1]),int(ope[2])+1):
            print(string[i],end="")
        print("")

