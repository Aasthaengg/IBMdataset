def main():
    s=list(input())
    k=int(input())
    i=0
    while k>=0 and i<len(s)-1:
        if s[i]!='a' and k>=123-ord(s[i]):
            k-=123-ord(s[i])
            s[i]="a"
        i+=1
    if i==len(s)-1:
        s[-1]=chr(97+(k-(123-ord(s[i])))%26)
    print("".join(s))
if __name__=="__main__":
    main()