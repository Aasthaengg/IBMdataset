def main():
    s=input()
    x=set(s)
    for i in x:
        if(s.count(i)%2==1):
            print('No')
            return;
    print('Yes')

main()
