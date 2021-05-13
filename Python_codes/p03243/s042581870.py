n=int(input())
l=[111,222,333,444,555,666,777,888,999]
for i in range(1000):
    if n in l:
        print(n)
        exit()
    n+=1

            
