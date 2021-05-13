T = input()
def gettotal(s):
    score = 0
    for i in range(len(s)):
        if s[i] == "D":
            score +=1        
        if i < len(s)-1:
            if s[i] + s[i+1] == "PD":
                score +=1
    return score

def pd(T):
    T = T.replace("?","D")
    print(T)
    #return gettotal(T)

pd(T)