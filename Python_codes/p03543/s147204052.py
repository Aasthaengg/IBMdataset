def main():
    a=input()
    b=set(a)
    if(len(b)<=2):
        if(a.count(a[1],0,3)!=3 and a.count(a[2],1,4)!=3):
            print('No')
        else:
            print('Yes')
    else:
        print('No')

main()
