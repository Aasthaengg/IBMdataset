def main():
    a=input()
    for i in range(1,len(a)):
        if(a[i]==a[i-1]):
            print("Bad")
            return;
    print("Good")

main()
