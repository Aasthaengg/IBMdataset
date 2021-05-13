s = input()
x, y = map(int, input().split())

def cul(x_axis,x):
    dic={0:1}
    for i in range(len(x_axis)):
        tmp={}
        for j in dic:
            tmp[j+x_axis[i]]=1
            tmp[j-x_axis[i]]=1
        dic=tmp
    if x in dic: return True
    else: return False

s_split = [len(item) for item in s.split("T")]

x_axis = s_split[0::2]
y_axis = s_split[1::2]

if s[0]=="F": x=abs(x-x_axis.pop(0))
y=abs(y)

print("Yes" if cul(x_axis,x) and cul(y_axis,y) else "No")