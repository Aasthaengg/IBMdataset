C=input()
result=1
lst=[]
lst.extend('abcdefghijklmnopqrstuvwxyz')
for i in lst:
    if i != C:
        result+=1
    else:
        result+=0
        break
print(lst[result])