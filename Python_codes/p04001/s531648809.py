S = input()

def saiki(n, s=S[0]):
    _sum = 0
    
    if n==len(S)-1:
#         print(s)
        return eval(s)
    
    _sum += saiki(n+1, s + "+" + S[n+1])
    _sum += saiki(n+1, s + S[n+1])
    
    return _sum
    
print(saiki(0))