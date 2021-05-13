S = input()

def saiki(i,s = S[0]):
    _sum = 0
    if i == len(S) - 1:
        ans = eval(s)
        return ans
    a = saiki(i + 1, s + "+" + S[i+1])
    b = saiki(i + 1, s + S[i+1])
    
    return a + b
    
print(saiki(0))
