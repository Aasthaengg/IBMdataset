N=input()
def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num
S=alpha2num(N)+1
num2alpha = lambda c: chr(c+64)

print(num2alpha(S))