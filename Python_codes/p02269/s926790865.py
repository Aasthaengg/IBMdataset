n=int(input())
dict={}
for i in range(n):
    str=input()
    if str[0]=="i":
        dict.update({str[7:]:1})
    else:
        if str[5:] in dict:
            print("yes")
        else:
            print("no")
