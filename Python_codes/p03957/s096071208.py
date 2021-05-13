def main():
    s=input()
    a=s.find('C')
    if(a==-1):
        print('No')
    else:
        a2=s.find('F',a+1,len(s))
        if(a2==-1):
            print('No')
        else:
            print('Yes')

main()
