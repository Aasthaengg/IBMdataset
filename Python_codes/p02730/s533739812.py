s=input()

def kaibun(w):
    for i in range(len(w)):
        if w[i]!=w[len(w)-1-i]:
            return False
    return True
n=len(s)
print("Yes") if all([kaibun(s) , kaibun(s[:(n-1)//2]) , kaibun(s[(n+3)//2-1:])]) else print("No")