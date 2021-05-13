if __name__ == '__main__':
    n = int(input())
    setN =set([n])
    count=1
    while True:
        if n %2 ==1:
            n=3*n+1
        else:
            n=n/2
        if n in setN:
            print(count+1)
            break
        else:
            count+=1
            setN.add(n)