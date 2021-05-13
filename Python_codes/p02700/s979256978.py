def main():
    A,B,C,D = map(int,input().split())
    temp = 0

    while A>0 and C>0:
        temp += 1
        if temp%2 == 1:
            C = C - B
        else:
            A -= D
        #print(temp,A,C)

    if temp%2 == 1:
        return 'Yes'
    else:
        return 'No'

print(main())
