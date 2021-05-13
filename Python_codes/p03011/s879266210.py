X=input()
a, b, c= map(str, X.split())
a ,b ,c=int(a), int(b), int(c)
test1=a+b
test2=a+c
test3=b+c
list=[]
list.append(test1)
list.append(test2)
list.append(test3)
print(min(list))