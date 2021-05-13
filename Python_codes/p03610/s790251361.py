s=str(input())

def ans072(s:str):
    ans_str=""
    for i in range(0,len(s)):
        if i%2==0:
            ans_str=ans_str+s[i]
    return ans_str

print(ans072(s))
