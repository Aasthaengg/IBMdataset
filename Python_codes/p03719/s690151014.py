def main():
    s = input().split()
    
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    
    if(a<=c and c<=b):
        print("Yes")
    else:
        print("No")
    
main()