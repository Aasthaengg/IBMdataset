n=int(input())

l=[111,222,333,444,555,666,777,888,999]

for i in range(len(l)):
    if n<= l[i]:
        print(l[i])
        break
