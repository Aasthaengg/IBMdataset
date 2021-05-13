def main():
    a=input()
    b=set(a)
    if(len(b)==2):
        if(a.count(b.pop())==2):
            if(a.count(b.pop())==2):
                print("Yes")
                return;
    print("No")

main()
