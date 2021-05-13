
k= int(input())
s= str(input())


if int(k)>=1 and int(k)<=100 and len(s)>=1 and len(s)<=100: #check if k and s are between 1 to 100

    if len(s) > k:

        print (s[:k]+"...") #cut the str until value of k and add ... to the end

    else:
        print (s)