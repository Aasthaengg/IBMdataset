def getinputdata():

    # 配列初期化
    array_result = []
    
    data = input()

    array_result.append(data.split(" "))

    flg = 1

    try:

        while flg:

            data = input()

            if(data != ""):
                
                array_result.append(data.split(" "))

            else:

                flg = 0
    finally:

        return array_result

arr_data = getinputdata()

s = arr_data[0][0]

kposi = s.find("K")
iposi = s.find("I")
hposi = s.find("H")
bposi = s.find("B")
rposi = s.find("R")


if len(s) >= 10:
    
    print("NO")
    
elif not((kposi == 0 or kposi == 1)  and 
#        kposi < iposi and 
#        iposi < hposi and 
#        hposi < bposi and 
#        bposi < rposi and 
        kposi == iposi-1 and 
        iposi == hposi-1 and 
        (hposi == bposi-1 or hposi == bposi-2) and 
        (bposi == rposi-1 or bposi == rposi-2) and 
        (s[-2::] == "RA" or s[-2::]=="BR" or s[-2::]=="AR")):

    print("NO")
    
elif not(s.count("K") == 1 and s.count("I") == 1 and s.count("H") == 1 and s.count("B") == 1 and s.count("R") == 1 and (s.count("A") == 0 or s.count("A") == 1 or s.count("A") == 2 or s.count("A") == 3 or s.count("A") == 4)):
    
    print("NO")
    
    
else:
    
    print("YES")

