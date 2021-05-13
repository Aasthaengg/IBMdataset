n=input()

def make_seven(n):
    al=[]
    for i in range(4):
        a=int(n[i])
        al.append(a)

    for j in range(-1,2,2):
        for k in range(-1,2,2):
            for l in range(-1,2,2):
                if al[0]+j*al[1]+k*al[2]+l*al[3]==7:
                    if j==-1:
                        o1="-"
                    else:
                        o1="+"
                    if k==-1:
                        o2="-"
                    else:
                        o2="+"
                    if l==-1:
                        o3="-"
                    else:
                        o3="+"
                    print(str(al[0])+o1+str(al[1])+o2+str(al[2])+o3+str(al[3])+"=7")
                    return
make_seven(n)