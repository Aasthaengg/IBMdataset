from sys import stdin,stdout


if __name__=="__main__":

    n=int(stdin.readline())
    b=[int(x) for x in stdin.readline().split()]
    b.append(1000000)

    s=b[0]

    for i in range(n-1):
        if b[i]>b[i+1]:
            s+=b[i+1]
        else:
            s+=b[i]
    stdout.write(str(s)+"\n")
    
