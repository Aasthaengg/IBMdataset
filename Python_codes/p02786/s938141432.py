#memo = [0] * 100000000
#memo[1] = 1

def saiki(n):
#    global memo
    tmp = 0
    if n <= 1:
        return 1
#        return memo[1]
    else:
        tmp = int(n/2)
        return saiki(tmp) * 2 + 1
#        if memo[tmp] == 0:
#            memo[tmp] = saiki(tmp)
#        return memo[tmp]+memo[tmp]+1
    
h = int(input())
print(saiki(h))
